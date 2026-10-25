# Team name: Group 3
# Team members: Erich Mundt, Addie Hurst
# Course and section: CS 2430, section 502
# Project name: Programming Project 2
# File: Fuzzy_report.py - prints verifiable fuzzy-set evidence.
# Run from the project root:  python Fuzzy_report.py
#
# For every test case and every element of the universe it prints the INPUT
# degrees, the EXPECTED result (worked out by hand in tests/test_fuzzy_sets.py),
# the ACTUAL result from the program, and PASS/FAIL. PASS means the actual and
# expected degrees differ by no more than TOLERANCE (see Fuzzy_sets.py).
# It also documents how invalid membership input is handled.

import sys

from Data import FUZZY_CASES, FUZZY_EDGE_CASES
from fuzzysets import FuzzySet, TOLERANCE
from Universe import UNIVERSE
from fuzzysets_test import EXPECTED      # hand-worked expected degrees

ALL_CASES = FUZZY_CASES + FUZZY_EDGE_CASES


def where(name, case):
    #Is the element stored in both inputs, one input, or neither (but in U)?
    in_a, in_b = name in case["A"], name in case["B"]
    return "both" if in_a and in_b else "only A" if in_a else "only B" if in_b else "neither"


def close(x, y):
    return abs(x - y) <= TOLERANCE


def report_case(case):
    #Print one case as a table; return (checks run, checks failed).
    a, b = FuzzySet.from_degrees(case["A"]), FuzzySet.from_degrees(case["B"])
    actual = {"not_a": a.complement(), "union": a.union(b), "inter": a.intersection(b)}
    want = EXPECTED[case["name"]]

    print(f"=== {case['name']} ===")
    print(f"Input A (stored entries): {case['A']}")
    print(f"Input B (stored entries): {case['B']}")
    print("Elements not stored in a set have degree 0.0.\n")
    print(f"{'elem':<5}{'in':<8}{'A(x)':>6}{'B(x)':>6} | "
          f"{'NOT A: exp':>11}{'act':>10} | {'UNION: exp':>11}{'act':>10} | "
          f"{'INTERSECT: exp':>15}{'act':>10} | result")
    checks = failures = 0
    for name in UNIVERSE:
        row_ok = True
        cells = []
        for key in ("not_a", "union", "inter"):
            exp, act = want[key].degree_of(name), actual[key].degree_of(name)
            cells.append((exp, act))
            row_ok = row_ok and close(exp, act)
            checks += 1
            failures += 0 if close(exp, act) else 1
        (e1, a1), (e2, a2), (e3, a3) = cells
        print(f"{name:<5}{where(name, case):<8}{a.degree_of(name):>6.2f}{b.degree_of(name):>6.2f} | "
              f"{e1:>11.6f}{a1:>10.6f} | {e2:>11.6f}{a2:>10.6f} | "
              f"{e3:>15.6f}{a3:>10.6f} | {'PASS' if row_ok else 'FAIL'}")
    print()
    return checks, failures


def report_invalid_input():
    #Document how invalid membership input is handled (each must raise ValueError).
    print("=== Invalid membership input (expected: ValueError, nothing stored) ===")
    bad_degrees = [("1.1  (above 1.0)", 1.1), ("-0.1 (below 0.0)", -0.1),
                   ("NaN", float("nan")), ("'0.5' (a string)", "0.5"),
                   ("None", None), ("True (a boolean)", True)]
    failures = 0
    for label, value in bad_degrees:
        try:
            FuzzySet.from_degrees({"a": value})
            outcome, ok = "ACCEPTED (wrong!)", False
        except ValueError as error:
            outcome, ok = f"ValueError: {error}", True
        failures += 0 if ok else 1
        print(f"  degree {label:<18} -> {outcome}")
    for label, action in [("unknown element 'z'", lambda: FuzzySet.from_degrees({"z": 0.5})),
                          ("array of wrong length", lambda: FuzzySet([0.5, 0.5]))]:
        try:
            action()
            outcome, ok = "ACCEPTED (wrong!)", False
        except ValueError as error:
            outcome, ok = f"ValueError: {error}", True
        failures += 0 if ok else 1
        print(f"  {label:<25} -> {outcome}")
    print()
    return failures


def main():
    print("##### FUZZY-SET VERIFICATION REPORT #####")
    print(f"Comparison tolerance: |actual - expected| <= {TOLERANCE}")
    print("(needed because floats are inexact, e.g. 1.0 - 0.7 = %r)\n" % (1.0 - 0.7))
    total = failed = 0
    for case in ALL_CASES:
        checks, failures = report_case(case)
        total, failed = total + checks, failed + failures
    failed += report_invalid_input()
    print(f"SUMMARY: {total} degree comparisons, {failed} failures "
          f"(including invalid-input checks)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())