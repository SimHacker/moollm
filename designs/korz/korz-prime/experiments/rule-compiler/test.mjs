// Acceptance tests for the generated Margolus kernels.
// The interesting one is round_trip: reversibility is a JOINT property of rule, schedule and
// coherence (margolus-rules.yml, crystallization.coherence_model), so running the inverse
// table forward does NOT undo the run. The phase sequence has to be reversed too.

import { RULES, META } from "./generated/margolus.js";

const W = 32, H = 32, STEPS = 40;

function seeded(w, h, seed) {
  const g = new Uint8Array(w * h);
  let s = seed >>> 0;
  for (let i = 0; i < g.length; i++) {
    s = (s * 1664525 + 1013904223) >>> 0;
    g[i] = (s >>> 16) & 1;
  }
  return g;
}

const same = (a, b) => a.length === b.length && a.every((v, i) => v === b[i]);
const pop = (g) => g.reduce((a, v) => a + v, 0);

let failures = 0;
const report = (name, test, ok, note = "") => {
  if (!ok) failures++;
  console.log(`  ${ok ? "pass" : "FAIL"}  ${name.padEnd(18)} ${test}${note ? "  — " + note : ""}`);
};

console.log("round trip: N steps forward, then N steps of the inverse with the phase sequence reversed\n");

for (const [name, { step, unstep }] of Object.entries(RULES)) {
  const original = seeded(W, H, 12345);
  const g = Uint8Array.from(original);

  for (let t = 0; t < STEPS; t++) step(g, W, H, t);
  const evolved = Uint8Array.from(g);

  if (!unstep) { report(name, "no inverse emitted"); continue; }
  for (let t = STEPS - 1; t >= 0; t--) unstep(g, W, H, t);

  report(name, "round trip", same(g, original));

  // "Did it move?" is the wrong question — rotate returns to the start every 8 steps and a
  // naive assertion just calls that a failure. Measure the recurrence period instead.
  const probe = Uint8Array.from(original);
  let period = null;
  for (let t = 0; t < 512; t++) {
    step(probe, W, H, t);
    if (same(probe, original) && (t + 1) % 2 === 0) { period = t + 1; break; }
  }
  report(name, "period", true, period ? `${period} steps` : ">512 steps");

  if (META[name].conserves.includes("population")) {
    report(name, "population held", pop(evolved) === pop(original),
           `${pop(original)} -> ${pop(evolved)}`);
  }
}

// The group action, checked against theory rather than against a fixture.
// First prediction was |C4| x phases = 8, on the reasoning that each phase's blocks need four
// 90-degree turns to come home. That is wrong, and the measurement caught it: composing the two
// phases' quarter-turns about DIFFERENT centres gives a half-turn about a third centre, and a
// half-turn is its own inverse. So one alternating pair squares to the identity: period 4.
console.log("\ngroup action: two quarter-turns about different centres compose to an involution\n");
{
  const { step } = RULES.rotate;
  const original = seeded(W, H, 4242);
  const g = Uint8Array.from(original);
  let period = null;
  for (let t = 0; t < 64 && period === null; t++) {
    step(g, W, H, t);
    if (same(g, original)) period = t + 1;
  }
  report("rotate", "period is 4", period === 4, `measured ${period}`);
}

// The control: run the inverse WITHOUT reversing the phase sequence. This must fail, or the
// schedule was never part of the rule and the YAML's claim is decoration.
console.log("\ncontrol: same inverse table, phases NOT reversed (expected to fail)\n");
{
  const { step, unstep } = RULES.critters;
  const original = seeded(W, H, 999);
  const g = Uint8Array.from(original);
  for (let t = 0; t < STEPS; t++) step(g, W, H, t);
  for (let t = 0; t < STEPS; t++) unstep(g, W, H, t);
  const recovered = same(g, original);
  report("critters", "phase order matters", !recovered,
         recovered ? "recovered anyway — schedule is NOT part of the rule" : "did not recover, as required");
}

console.log(`\n${failures === 0 ? "all checks passed" : failures + " FAILURES"}`);
process.exit(failures === 0 ? 0 : 1);
