// Assignment 2's published spec, as contracts.
//
// The build already owns compilation, accessibility, internal links, dangling
// content refs and deck syntax; `data-integrity.test.ts` owns "dated material
// stays inside the teaching period". These are the promises *my course* makes
// that neither of those can see.
//
// Spec lines only a person can judge — whether the course is genuinely niche,
// whether twelve weeks cohere into one idea, whether the prose has a voice, and
// whether it reads well at both marking viewports — are deliberately absent.
// They're settled at the crit, not here.
import { existsSync, readFileSync, readdirSync } from "node:fs";
import { resolve } from "node:path";
import { describe, expect, it } from "vitest";

interface ApiNode {
  id: string;
  type: string;
  title?: string;
  meta?: Record<string, unknown>;
}

interface CourseEdge {
  from: string;
  to: string;
}

interface CourseApi {
  edges?: CourseEdge[];
  course: {
    code: string;
    title: string;
    description: string;
    tags: string[];
    level: number;
  };
  nodes: ApiNode[];
}

const api = JSON.parse(readFileSync(resolve("dist/api/index.json"), "utf8")) as CourseApi;

const nodesOfType = (type: string): ApiNode[] => api.nodes.filter((n) => n.type === type);

/** The three digits this repo was provisioned with. No other course has them. */
const ALLOCATED_DIGITS = "233";

/** How many teaching weeks the course runs for. */
const TEACHING_WEEKS = 12;

describe("the course record", () => {
  it("keeps the three digits this repo was allocated", () => {
    expect(api.course.code).toMatch(/^SLOP[123468]\d{3}$/);
    expect(
      api.course.code.slice(-3),
      `the code must end in ${ALLOCATED_DIGITS} — only the level digit is mine to choose`,
    ).toBe(ALLOCATED_DIGITS);
  });

  it("declares a level matching the code's first digit", () => {
    expect(api.course.level).toBe(Number(api.course.code.at(4)));
  });

  // check:evidence greps for the STARTER_CONTENT marker comment, so deleting
  // the comment without replacing the prose under it passes that gate. This is
  // the assertion that closes the gap.
  it("is my course, not the starter's placeholders", () => {
    expect(api.course.title).not.toMatch(/Course Title Goes Here/i);
    expect(api.course.description).not.toMatch(/One concise paragraph explaining/i);
    expect(api.course.tags).not.toContain("replace me");
    expect(api.course.tags.length).toBeGreaterThan(0);
  });
});

describe("twelve dated teaching weeks", () => {
  const teaching = [...nodesOfType("sessions"), ...nodesOfType("lectures")];

  it("carries teaching material in every week from 1 to 12", () => {
    const weeks = new Set(
      teaching.map((n) => n.meta?.week).filter((w): w is number => typeof w === "number"),
    );
    const missing = Array.from({ length: TEACHING_WEEKS }, (_, i) => i + 1).filter(
      (w) => !weeks.has(w),
    );
    expect(missing, `no teaching material in week(s) ${missing.join(", ")}`).toEqual([]);
  });

  it("dates every piece of teaching material", () => {
    for (const node of teaching) {
      expect(String(node.meta?.date ?? ""), `${node.id} has no date`).toMatch(
        /^\d{4}-\d{2}-\d{2}/,
      );
    }
  });

  it("runs no teaching material past week 12", () => {
    const overrun = teaching.filter(
      (n) => typeof n.meta?.week === "number" && n.meta.week > TEACHING_WEEKS,
    );
    expect(overrun.map((n) => n.id), "teaching material beyond week 12").toEqual([]);
  });
});

describe("at least one lecture carries a real deck", () => {
  const withSlides = nodesOfType("lectures").filter(
    (n) => typeof n.meta?.slides === "string" && n.meta.slides !== "",
  );

  it("has a lecture declaring a deck", () => {
    expect(withSlides.length, "no lecture links a deck").toBeGreaterThan(0);
  });

  it("builds every deck a lecture links, and links it from the lecture page", () => {
    for (const lecture of withSlides) {
      const slides = String(lecture.meta?.slides);
      const deck = slides.replace(/^\/|\/$/g, ""); // "decks/week-01"
      expect(
        existsSync(resolve("dist", deck, "index.html")),
        `${lecture.id} links ${slides}, which did not build`,
      ).toBe(true);

      const page = resolve("dist", lecture.id, "index.html");
      expect(existsSync(page), `${lecture.id} did not build a page`).toBe(true);
      expect(
        readFileSync(page, "utf8"),
        `${lecture.id}'s page does not link its deck`,
      ).toContain(`${deck}/`);
    }
  });

  it("ships a deck with real slides in it, not just the starter's one", () => {
    const deckSources = withSlides.map((l) =>
      resolve("src/decks", `${String(l.meta?.slides).replace(/^\/decks\/|\/$/g, "")}.deck.mdx`),
    );
    const realDeck = deckSources.some((src) => {
      if (!existsSync(src)) return false;
      const body = readFileSync(src, "utf8");
      // `---` between slides; a deck worth linking has more than a title card.
      return body.split(/^---$/m).length >= 4 && !body.includes("STARTER_CONTENT");
    });
    expect(realDeck, "no linked deck has real slides in it").toBe(true);
  });
});

describe("assessment", () => {
  it("adds up to 100%", () => {
    const assessments = nodesOfType("assessments");
    expect(assessments.length, "the course has no assessment").toBeGreaterThan(0);

    const weights = assessments.map((a) => {
      const w = a.meta?.weight;
      expect(typeof w, `${a.id} has no numeric weight`).toBe("number");
      return w as number;
    });
    const total = weights.reduce((sum, w) => sum + w, 0);
    expect(total, `weights total ${total}%`).toBe(100);
  });

  // Named for what it actually asserts. That the date falls inside the teaching
  // period is a different claim, and it belongs to data-integrity.test.ts,
  // which owns it for every dated node rather than for assessments alone.
  it("gives every assessment a due date", () => {
    for (const a of nodesOfType("assessments")) {
      expect(String(a.meta?.due ?? ""), `${a.id} has no due date`).toMatch(/^\d{4}-\d{2}-\d{2}/);
    }
  });
});

// The course's defining structural claim, from CLAUDE.md: "if a week could be
// moved anywhere in the order without loss, it isn't carrying its part of the
// argument." That is a claim about the content, so it gets asserted against the
// content rather than left as a sentence in the harness.
describe("the argument is a chain, not twelve independent weeks", () => {
  const sessions = nodesOfType("sessions");
  const edges = api.edges ?? [];
  const weekOf = new Map(sessions.map((s) => [s.id, s.meta?.week as number]));

  /** Session-to-session edges pointing from a later week to an earlier one. */
  const backEdges = edges.filter((e) => {
    const from = weekOf.get(e.from);
    const to = weekOf.get(e.to);
    return typeof from === "number" && typeof to === "number" && to < from;
  });

  it("has every week after the first depending on an earlier one", () => {
    const dependent = new Set(backEdges.map((e) => e.from));
    const orphans = sessions
      .filter((s) => (s.meta?.week as number) > 1 && !dependent.has(s.id))
      .map((s) => s.id);
    expect(
      orphans,
      `these weeks declare no dependency on any earlier week, so they could be moved anywhere in the order: ${orphans.join(", ")}`,
    ).toEqual([]);
  });

  it("keeps week 1 as the root", () => {
    const first = sessions.find((s) => s.meta?.week === 1);
    expect(first, "no week 1").toBeDefined();
    expect(
      backEdges.some((e) => e.from === first?.id),
      "week 1 depends on an earlier week, which cannot be right",
    ).toBe(false);
  });

  it("closes the loop: the last week reaches back to the first", () => {
    const last = sessions.find((s) => s.meta?.week === 12);
    const reaches = backEdges.filter((e) => e.from === last?.id).map((e) => weekOf.get(e.to));
    expect(reaches, "week 12 declares no dependencies").not.toEqual([]);
    expect(
      reaches.includes(1),
      "week 12 does not reach back to week 1, and the whole course is built on it doing so",
    ).toBe(true);
  });
});

// Every week promises primary literature, on the home page and on the seminars
// index. This asserts the promise is kept, since a reading list is the kind of
// thing that quietly rots one week at a time.
describe("every teaching week carries its reading", () => {
  const sessions = nodesOfType("sessions");

  it("lists at least three resolvable sources per week", () => {
    const thin: string[] = [];
    for (const session of sessions) {
      const page = resolve("dist", session.id, "index.html");
      expect(existsSync(page), `${session.id} did not build`).toBe(true);
      const dois = readFileSync(page, "utf8").match(/https:\/\/doi\.org\/10\./g) ?? [];
      if (dois.length < 3) thin.push(`${session.id} (${dois.length})`);
    }
    expect(thin, `weeks with fewer than three linked sources: ${thin.join(", ")}`).toEqual([]);
  });
});

// The starter's listing pages addressed me, the person building the site, and
// carried no STARTER_CONTENT marker — so check:evidence could not see them and
// they shipped as course prose. This is the assertion that closes that gap, and
// it is deliberately about the reader rather than about any one phrase.
describe("no page talks to the author instead of the reader", () => {
  const authorFacing = [
    "src/site-config.ts",
    "src/content.config.ts",
    "Weights should sum to",
    "A course decides how many",
    "the language your course deserves",
    "replace the placeholder",
    "YOUR-REPO",
  ];

  it("keeps builder instructions out of the built site", () => {
    const pages = [
      "index.html",
      "sessions/index.html",
      "lectures/index.html",
      "assessments/index.html",
      "people/index.html",
      "policies/index.html",
      "schedule/index.html",
      "evidence/index.html",
    ];
    const offenders: string[] = [];
    for (const page of pages) {
      const path = resolve("dist", page);
      if (!existsSync(path)) continue;
      const html = readFileSync(path, "utf8");
      for (const phrase of authorFacing) {
        if (html.includes(phrase)) offenders.push(`${page}: "${phrase}"`);
      }
    }
    expect(offenders, `builder-facing text on public pages:\n${offenders.join("\n")}`).toEqual([]);
  });
});

// The theme's hero renders its <h1> only when a hero image resolves. This
// course is image-free by design, which silently removed the page title from
// four pages before anyone noticed — the design decision and the missing
// heading were separated by two layers of template. Every page a reader can
// land on needs exactly one top-level heading, so that is asserted rather than
// trusted.
describe("every page has exactly one h1", () => {
  const pageFiles = (dir: string, prefix = ""): string[] => {
    const out: string[] = [];
    for (const entry of readdirSync(dir, { withFileTypes: true })) {
      if (entry.name.startsWith("_") || entry.name === "api") continue;
      if (entry.isDirectory()) out.push(...pageFiles(resolve(dir, entry.name), `${prefix}${entry.name}/`));
      else if (entry.name.endsWith(".html")) out.push(`${prefix}${entry.name}`);
    }
    return out;
  };

  it("gives each built page one and only one top-level heading", () => {
    const wrong: string[] = [];
    for (const page of pageFiles(resolve("dist"))) {
      // Decks are slide documents; their heading structure is astromotion's.
      if (page.startsWith("decks/")) continue;
      const html = readFileSync(resolve("dist", page), "utf8");
      const count = (html.match(/<h1[\s>]/g) ?? []).length;
      if (count !== 1) wrong.push(`${page} has ${count}`);
    }
    expect(wrong, `pages without exactly one h1:\n${wrong.join("\n")}`).toEqual([]);
  });
});
