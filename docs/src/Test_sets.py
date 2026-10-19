# Team name: Group 3
# Team members: Erich Mundt, Addie Hurst
# Course and section: CS 2430, section 502
# Project name: Programming Project 2
# Primary author:
# File: tests/test_sets.py - verification for Part 1 (ordinary sets).
# Run from the project root:  python -m unittest -v
#
# Three kinds of checks:
#   1. Hand worked answers (worked out on paper, written as bit strings),
#   2. a cross-check against Python's built-in set type,
#   3. error handling and edge cases.

import unittest

from Sets_bitstring import BitSet
from Universe import UNIVERSE
from Data import SET_CASES, SET_EDGE_CASES

# Universe order: a b c d e f g h i j  (index 0 = leftmost bit)
# Expected results worked out by hand, per case name in data.py.
EXPECTED = {
    "overlapping": {  # A={a..e}, B={d,e,f,g}
        "not_a": "0000011111", "union": "1111111000", "inter": "0001100000",
        "a_minus_b": "1110000000", "sym": "1110011000"},
    "disjoint": {  # A={a,b,c}, B={f,g,h}
        "not_a": "0001111111", "union": "1110011100", "inter": "0000000000",
        "a_minus_b": "1110000000", "sym": "1110011100"},
    "A is a subset of B": {  # A={b,c}, B={a,b,c,d}
        "not_a": "1001111111", "union": "1111000000", "inter": "0110000000",
        "a_minus_b": "0000000000", "sym": "1001000000"},
    "edge: A is the empty set": {  # A={}, B={a,c,e}
        "not_a": "1111111111", "union": "1010100000", "inter": "0000000000",
        "a_minus_b": "0000000000", "sym": "1010100000"},
    "edge: A is the full universe": {  # A=everything, B={a,c,e}
        "not_a": "0000000000", "union": "1111111111", "inter": "1010100000",
        "a_minus_b": "0101011111", "sym": "0101011111"},
    "edge: A equals B": {  # A=B={b,d,f}
        "not_a": "1010101111", "union": "0101010000", "inter": "0101010000",
        "a_minus_b": "0000000000", "sym": "0000000000"},
}

ALL_CASES = SET_CASES + SET_EDGE_CASES


class TestHandWorkedResults(unittest.TestCase):
    def test_every_operation_matches_hand_work(self):
        for case in ALL_CASES:
            with self.subTest(case=case["name"]):
                a = BitSet.from_names(case["A"])
                b = BitSet.from_names(case["B"])
                want = EXPECTED[case["name"]]
                self.assertEqual(a.complement().to_bit_string(), want["not_a"])
                self.assertEqual(a.union(b).to_bit_string(), want["union"])
                self.assertEqual(a.intersection(b).to_bit_string(), want["inter"])
                self.assertEqual(a.difference(b).to_bit_string(), want["a_minus_b"])
                self.assertEqual(a.symmetric_difference(b).to_bit_string(), want["sym"])


class TestAgainstPythonSets(unittest.TestCase):
    # Independent cross-check: Python's set type must give the same elements.

    def test_matches_builtin_set_operations(self):
        universe = set(UNIVERSE)
        for case in ALL_CASES:
            with self.subTest(case=case["name"]):
                a_names, b_names = set(case["A"]), set(case["B"])
                a, b = BitSet.from_names(a_names), BitSet.from_names(b_names)
                self.assertEqual(set(a.complement().to_names()), universe - a_names)
                self.assertEqual(set(a.union(b).to_names()), a_names | b_names)
                self.assertEqual(set(a.intersection(b).to_names()), a_names & b_names)
                self.assertEqual(set(a.difference(b).to_names()), a_names - b_names)
                self.assertEqual(set(a.symmetric_difference(b).to_names()),
                                 a_names ^ b_names)


class TestEdgeCasesAndProperties(unittest.TestCase):
    def test_universe_has_at_least_ten_elements(self):
        self.assertGreaterEqual(len(UNIVERSE), 10)

    def test_complement_of_empty_is_full_and_back(self):
        empty = BitSet.from_names([])
        full = BitSet.from_names(UNIVERSE)
        self.assertEqual(empty.complement(), full)
        self.assertEqual(full.complement(), empty)

    def test_double_complement_returns_original(self):
        a = BitSet.from_names(["a", "d", "j"])
        self.assertEqual(a.complement().complement(), a)

    def test_symmetric_difference_with_itself_is_empty(self):
        a = BitSet.from_names(["b", "d", "f"])
        self.assertEqual(a.symmetric_difference(a), BitSet.from_names([]))

    def test_operations_do_not_modify_their_inputs(self):
        a = BitSet.from_names(["a", "b"])
        b = BitSet.from_names(["b", "c"])
        before = (a.to_bit_string(), b.to_bit_string())
        a.union(b);
        a.intersection(b);
        a.difference(b)
        a.symmetric_difference(b);
        a.complement()
        self.assertEqual((a.to_bit_string(), b.to_bit_string()), before)


class TestInvalidInput(unittest.TestCase):
    def test_unknown_element_name_rejected(self):
        with self.assertRaises(ValueError):
            BitSet.from_names(["z"])

    def test_wrong_length_bits_rejected(self):
        with self.assertRaises(ValueError):
            BitSet([True, False])

    def test_non_boolean_bit_rejected(self):
        with self.assertRaises(ValueError):
            BitSet([2] + [0] * (len(UNIVERSE) - 1))

    def test_operating_on_non_set_rejected(self):
        with self.assertRaises(TypeError):
            BitSet.from_names(["a"]).union({"a"})


if __name__ == "__main__":
    unittest.main()