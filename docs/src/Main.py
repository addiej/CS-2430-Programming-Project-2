# Team name: Group 3
# Team members: Erich Mundt, Addie Hurst
# Course and section: CS 2430, section 502
# Project name: Programming Project 2
# File: main.py - runs every demo with clearly labeled output.
# Run with:  python main.py

from Data import SET_CASES, SET_EDGE_CASES, MULTISET_CASES, MULTISET_EDGE_CASES, FUZZY_CASES, FUZZY_EDGE_CASES
from Sets_bitstring import BitSet
from multisets import MultiSet
from Formatting import format_universe, format_set, format_multiset, format_fuzzy
from fuzzysets import FuzzySet


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

#Runs the Part 2 multiset operations and displays their results.
def run_multiset_case(case):
    # Builds this case's A and B from {element name: count}, then shows all four operations.
    a = MultiSet.from_counts(case["A"])
    b = MultiSet.from_counts(case["B"])

    print(f"=== Part 2 case: {case['name']} ===")
    print(format_multiset("A (input)", a))
    print(format_multiset("B (input)", b))
    print(format_multiset("A UNION B = max counts", a.union(b)))
    print(format_multiset("A INTERSECT B = min counts", a.intersection(b)))
    print(format_multiset("A MINUS B = A - B, not below 0", a.difference(b)))
    print(format_multiset("A SUM B = counts added", a.sum(b)))
    print()

def run_part2():
    print("##### PART 2: MULTISETS (counts) #####")
    for case in MULTISET_CASES + MULTISET_EDGE_CASES:
         run_multiset_case(case)

def run_fuzzy_case(case):
    # Shows one fuzzy case: the inputs, then complement, union, and intersection.
    a = FuzzySet.from_degrees(case["A"])
    b = FuzzySet.from_degrees(case["B"])

    print(f"=== Fuzzy case: {case['name']} ===")
    print(format_fuzzy("A (input)", a))
    print(format_fuzzy("B (input)", b))
    print(format_fuzzy("COMPLEMENT of A = 1 - A(x)", a.complement()))
    print(format_fuzzy("A UNION B = max(A(x), B(x))", a.union(b)))
    print(format_fuzzy("A INTERSECT B = min(A(x), B(x))", a.intersection(b)))
    print()


def run_fuzzy():
    # Change Request demo: representative cases first, then edge cases.
    print("##### CHANGE REQUEST: FUZZY SETS #####")
    print(format_universe())
    print()
    for case in FUZZY_CASES + FUZZY_EDGE_CASES:
        run_fuzzy_case(case)


def main():
    run_part1()
    run_part2()
    run_fuzzy()

if __name__ == "__main__":
    main()
