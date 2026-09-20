#!/usr/bin/env node
/**
 * Slide-fit check for the decks.
 *
 * The known blind spot: "Nothing checks whether a slide fits or stays legible;
 * that only shows up in a browser." The build compiles every deck and astromotion
 * validates its structure, but neither can see whether a slide's content is
 * taller than the slide. Reveal clips the overflow rather than scrolling it, so
 * a slide can lose its last line — in practice its conclusion — and every check
 * stays green. It found five such slides the first time it ran, and in all five
 * the clipped part was the claim the diagram existed to make.
 *
 * Reveal lays each slide out in a fixed 1280x720 logical box and scales that box
 * to the window, so fit is viewport-independent: a slide that fits at 1920x1080
 * fits at 390x844, just smaller. This measures fit once. Whether a slide is
 * *legible* once scaled onto a phone is a judgement call and stays a human one.
 *
 * Method: serve dist/, open one driver page in headless Chrome, and let it walk
 * every slide of every deck by hash, comparing each slide's content extent to
 * the box it has to fit inside. The driver POSTs its results back to the same
 * server, which is the part that matters: `--dump-dom` never returns for a page
 * that has run a few hundred timers, so reading the answer off the wire is what
 * makes this terminate. No new dependencies.
 *
 *   pnpm build && node scripts/deck-fit.mjs
 *   CHROME=/path/to/chrome node scripts/deck-fit.mjs --port 4401
 */
import { spawn } from "node:child_process";
import { mkdtempSync, readFileSync, readdirSync, rmSync, writeFileSync } from "node:fs";
import { createServer } from "node:http";
import { tmpdir } from "node:os";
import { extname, join, resolve } from "node:path";

const CHROME =
  process.env.CHROME ?? "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const portArg = process.argv.indexOf("--port");
const PORT = portArg > -1 ? Number(process.argv[portArg + 1]) : 4394;

/** The deployed base path, read back out of the build's own asset URLs. */
const base = (() => {
  const home = readFileSync(resolve("dist/index.html"), "utf8");
  const m = /["'(](\/[^"'()\s]*?)\/_astro\//.exec(home);
  return m ? `${m[1]}/` : "/";
})();
const prefix = base.replace(/\/$/, "");

const decks = readdirSync(resolve("dist/decks"), { withFileTypes: true })
  .filter((e) => e.isDirectory())
  .map((e) => e.name)
  .sort();

if (decks.length === 0) {
  console.error("no decks in dist/decks — run `pnpm build` first");
  process.exit(1);
}

const MIME = {
  ".html": "text/html; charset=utf-8", ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8", ".json": "application/json; charset=utf-8",
  ".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg",
  ".avif": "image/avif", ".webp": "image/webp", ".woff2": "font/woff2",
  ".txt": "text/plain; charset=utf-8",
};
let resolveResult;
let served = 0;
/** One POST per deck, so a result is banked as soon as it exists. */
const collected = [];
const resultReady = new Promise((r) => { resolveResult = r; });

const server = createServer((req, res) => {
  try {
    let p = decodeURIComponent(new URL(req.url, "http://localhost").pathname);
    // The driver posts its measurements back here. Reading them off the wire
    // rather than out of `--dump-dom` is what makes this finish: Chrome asked
    // to dump the DOM of a page that ran a few hundred timers never returned.
    if (req.method === "POST" && p.endsWith("/__deck-fit")) {
      let body = "";
      req.on("data", (c) => { body += c; });
      req.on("end", () => {
        res.writeHead(204).end();
        try {
          const msg = JSON.parse(body);
          if (msg.error) return void resolveResult({ error: msg.error });
          collected.push(msg);
          if (collected.length === decks.length) resolveResult({ rows: collected });
        } catch (err) {
          resolveResult({ error: `unreadable result: ${String(err)}` });
        }
      });
      return;
    }
    if (prefix && p.startsWith(prefix)) p = p.slice(prefix.length);
    if (p === "" || p.endsWith("/")) p += "index.html";
    const file = resolve("dist" + p);
    if (!file.startsWith(resolve("dist"))) return void res.writeHead(403).end();
    // Read before writing the header: Chrome asks for things that are not there
    // (favicons, source maps), and a throw after writeHead is an unrecoverable
    // ERR_HTTP_HEADERS_SENT rather than a 404.
    const body = readFileSync(file);
    res.writeHead(200, { "content-type": MIME[extname(file)] ?? "application/octet-stream" });
    served += 1;
    res.end(body);
  } catch {
    if (!res.headersSent) res.writeHead(404, { "content-type": "text/plain" });
    res.end("not found");
  }
});
await new Promise((r) => server.listen(PORT, "127.0.0.1", r));

const driver = resolve("dist/_deck-fit.html");
writeFileSync(driver, `<!doctype html><meta charset=utf-8><div id=out></div>
<iframe id=f style="position:fixed;left:-9999px;top:0;width:1600px;height:900px"></iframe><script>
const BASE=${JSON.stringify(prefix + "/decks/")}, DECKS=${JSON.stringify(decks)};
const f=document.getElementById('f'), out=document.getElementById('out');
const rows=[]; const sleep=ms=>new Promise(r=>setTimeout(r,ms));
(async()=>{
  for(const deck of DECKS){
    // astromotion shows a one-time help card per deck; pre-claim it so it never paints.
    try{ sessionStorage.setItem('astromotion:help-seen:'+BASE+deck+'/','1'); }catch(e){}
    await new Promise(res=>{ f.onload=res; f.src=BASE+deck+'/'; });
    await sleep(500);
    const doc=f.contentDocument, win=f.contentWindow;
    const total=doc.querySelectorAll('.slides > section').length;
    let max=0; const bad=[];
    for(let i=1;i<=total;i++){            // reveal's hash index is 1-based here
      win.location.hash='#/'+i; await sleep(45);
      const sec=doc.querySelector('section.present'); if(!sec) continue;
      const box=sec.getBoundingClientRect(); if(!box.height) continue;
      let top=box.bottom, bot=box.top;
      for(const el of sec.children){ const r=el.getBoundingClientRect();
        if(!r.height && !r.width) continue;
        if(r.top<top) top=r.top; if(r.bottom>bot) bot=r.bottom; }
      const used=(bot-top)/box.height;
      if(used>max) max=used;
      if(used>1.0){
        const h=((sec.querySelector('h1,h2,h3'))||{}).textContent||'(no heading)';
        bad.push({slide:i, pct:Math.round(used*100), heading:h.replace('#','').trim().slice(0,60)});
      }
    }
    const row={deck, total, max:Math.round(max*100), bad};
    rows.push(row);
    // Beacon rather than fetch, and once per deck rather than once at the end:
    // under --virtual-time-budget a trailing fetch can be cut off before it
    // resolves, and a banked result is worth more than a tidy one.
    navigator.sendBeacon('__deck-fit', JSON.stringify(row));
  }
  out.textContent='@@'+JSON.stringify(rows)+'@@';
})().catch(e=>navigator.sendBeacon('__deck-fit',JSON.stringify({error:String((e&&e.message)||e)})));
</script>`);

const profile = mkdtempSync(join(tmpdir(), "deckfit-"));
const cleanup = () => {
  server.close();
  try { rmSync(profile, { recursive: true, force: true }); } catch {}
  try { rmSync(driver, { force: true }); } catch {}
};

const budget = 20000 + decks.length * 14000;
// --virtual-time-budget is what keeps headless Chrome alive and advances the
// driver's timers quickly; without it, headless given no output action exits
// as soon as the page has loaded. It is NOT paired with --dump-dom here: that
// combination is what hung.
const chrome = spawn(CHROME, [
  "--headless", "--disable-gpu", "--no-first-run", "--hide-scrollbars",
  `--user-data-dir=${profile}`, "--window-size=1600,900",
  `--virtual-time-budget=${budget}`,
  // --screenshot is load-bearing, oddly: Chrome given an output action waits
  // out the virtual-time budget and exits cleanly, where the same run with
  // --dump-dom, or with no action at all, does not. The PNG is a by-product.
  `--screenshot=${join(profile, "deck-fit.png")}`,
  `http://localhost:${PORT}${prefix}/_deck-fit.html`,
], { stdio: "ignore" });

let chromeFailed = null;
chrome.on("error", (err) => { chromeFailed = err; resolveResult(null); });

const timeout = new Promise((r) => setTimeout(() => r(null), 180000));
const payload = await Promise.race([resultReady, timeout]);
chrome.kill("SIGKILL");

cleanup();

if (chromeFailed) {
  console.error(`could not run Chrome at ${CHROME} — set CHROME=/path/to/chrome`);
  process.exit(1);
}
if (!payload) {
  console.error(
    `driver posted no measurements before the deadline (${served} file(s) served — ` +
      `${served === 0 ? "Chrome never fetched the driver" : "the driver ran but did not finish"})`,
  );
  process.exit(1);
}
const parsed = payload;
if (parsed.error) {
  console.error(`driver failed: ${parsed.error}`);
  process.exit(1);
}
const rows = parsed.rows;
let slides = 0;
const failures = [];
for (const r of rows) {
  slides += r.total;
  const flag = r.bad.length ? `  -- ${r.bad.length} OVERFLOWING` : "";
  console.log(`  ${r.deck}: ${r.total} slides, tallest uses ${r.max}%${flag}`);
  for (const b of r.bad) {
    console.log(`      #${b.slide}  ${b.pct}% of slide height  ${b.heading}`);
    failures.push(`${r.deck} #${b.slide}`);
  }
}

if (failures.length === 0) {
  console.log(`✓ decks: ${slides} slides across ${rows.length} deck(s) all fit`);
  process.exit(0);
}
console.error(`\n${failures.length} slide(s) overflow their box: ${failures.join(", ")}`);
process.exit(1);
