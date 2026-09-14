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
import { existsSync, readFileSync } from "node:fs";
import { resolve } from "node:path";
import { describe, expect, it } from "vitest";

interface ApiNode {
  id: string;
  type: string;
  title?: string;
  meta?: Record<string, unknown>;
}

interface CourseApi {
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

  it("gives every assessment a due date inside the teaching period", () => {
    for (const a of nodesOfType("assessments")) {
      expect(String(a.meta?.due ?? ""), `${a.id} has no due date`).toMatch(/^\d{4}-\d{2}-\d{2}/);
    }
  });
});
