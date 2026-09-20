/**
 * The four parts of the argument.
 *
 * The course's claim is that the order is load-bearing, so which part a week
 * belongs to is a fact about the curriculum rather than a presentational
 * detail. It lives here because the schedule page and each week's own page both
 * state it, and two copies of a fact are two chances to disagree.
 */
export interface CoursePart {
  numeral: string;
  title: string;
  /** Inclusive week range. */
  from: number;
  to: number;
}

export const courseParts: CoursePart[] = [
  { numeral: "I", title: "The premise", from: 1, to: 2 },
  { numeral: "II", title: "Interior models", from: 3, to: 7 },
  { numeral: "III", title: "The control group", from: 8, to: 10 },
  { numeral: "IV", title: "The human case, and its limits", from: 11, to: 12 },
];

export function partForWeek(week: number): CoursePart | undefined {
  return courseParts.find((p) => week >= p.from && week <= p.to);
}

/** "Part II — Interior models", or undefined for a week outside the teaching period. */
export function partLabel(week: number): string | undefined {
  const part = partForWeek(week);
  return part ? `Part ${part.numeral} — ${part.title}` : undefined;
}
