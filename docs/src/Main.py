# Team name: Erich Mundt
# Team members: Erich Mundt, Addie Hurst
# Course and section: CS 2430, section 502
# Project name: Programming Project 2
# Primary author:
# File: main.py - runs every demo with clearly labeled output.
# Run with:  python main.py

from Data import SET_CASES, SET_EDGE_CASES
from Sets_bitstring import BitSet
from Formatting import format_universe, format_set


def run_set_case(case):
    #Show one Part 1 case: the inputs, then all five operations.
    a = BitSet.from_names(case["A"])
    b = BitSet.from_names(case["B"])

    print(f"=== Part 1 case: {case['name']} ===")
    print(format_set("A (input)", a))
    print(format_set("B (input)", b))
    print(format_set("NOT(A)", a.complement()))
    print(format_set("A UNION B", a.union(b)))
    print(format_set("A INTERSECT B", a.intersection(b)))
    print(format_set("A MINUS B", a.difference(b)))
    print(format_set("A SYMMETRIC DIFFERENCE B = (A-B) U (B-A)",
                     a.symmetric_difference(b)))
    print()


def run_part1():
    #Part 1 demo: representative cases first, then edge cases.
    print("PART 1: ORDINARY SETS (bit strings) #####")
    print(format_universe())
    print()
    for case in SET_CASES + SET_EDGE_CASES:
        run_set_case(case)


def main():
    run_part1()


if __name__ == "__main__":
    main()