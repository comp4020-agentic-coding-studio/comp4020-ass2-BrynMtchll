// A sensor, not a contract test. The build runs axe over the decks as well as
// the pages, and an empty leading table header fails it -- but only after a
// full build, with a message that names the page and not the line. I have now
// written `| | header |` three times, so this catches it at the source.
import { readFileSync } from "node:fs";
import { globSync } from "node:fs";
import { resolve } from "node:path";
import { describe, expect, it } from "vitest";

const decks = globSync("src/decks/*.deck.mdx");

describe("deck tables", () => {
  it("finds every deck source", () => {
    expect(decks.length).toBeGreaterThan(0);
  });

  it("gives every table header cell discernible text", () => {
    const offences: string[] = [];
    for (const file of decks) {
      const lines = readFileSync(resolve(file), "utf8").split("\n");
      lines.forEach((line, i) => {
        if (!line.trimStart().startsWith("|")) return;
        const next = lines[i + 1] ?? "";
        // a header row is the line immediately above the --- separator row
        if (!/^\s*\|[\s:|-]+\|\s*$/.test(next)) return;
        const cells = line.trim().replace(/^\||\|$/g, "").split("|");
        if (cells.some((c) => c.trim() === "")) {
          offences.push(`${file}:${i + 1}  ${line.trim()}`);
        }
      });
    }
    expect(offences, `empty table header cell — axe rejects this:\n${offences.join("\n")}`)
      .toEqual([]);
  });
});
