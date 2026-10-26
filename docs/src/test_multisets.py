# Team name: Group 3
# Team members: Erich Mundt, Addie Hurst
# Course and section: CS 2430, section 502
# Project name: Programming Project 2
# File: tests/test_multisets.py - verification for Part 2 (multisets).
# Run from the project root:  python -m unittest -v
#
# Checks: (1) hand-worked expected counts, (2) cross-check against Python's
# collections.Counter (whose | & - + match max, min, truncated difference, sum),
# (3) both A and B have at least two counts above 1, (4) edge cases and errors.

import unittest
from collections import Counter

from Data import MULTISET_CASES, MULTISET_EDGE_CASES
from multisets import MultiSet
from Universe import UNIVERSE

# Expected results worked out by hand ({name: count}; unlisted = 0).
EXPECTED = {
    "overlapping counts": {
        "union": {"a": 3, "b": 5, "c": 1, "d": 2, "e": 4},
        "inter": {"a": 1, "b": 2, "e": 2},
        "diff":  {"a": 2, "c": 1, "e": 2},
        "sum":   {"a": 4, "b": 7, "c": 1, "d": 2, "e": 6}},
    "elements only in one multiset": {
        "union": {"a": 2, "b": 3, "c": 2, "d": 4},
        "inter": {},
        "diff":  {"a": 2, "b": 3},
        "sum":   {"a": 2, "b": 3, "c": 2, "d": 4}},
    "identical multisets": {
        "union": {"a": 2, "c": 3, "f": 1},
        "inter": {"a": 2, "c": 3, "f": 1},
        "diff":  {},
        "sum":   {"a": 4, "c": 6, "f": 2}},
    "edge: B counts exceed A (difference clamps at 0)": {
        "union": {"a": 4, "b": 2, "c": 3},
        "inter": {"a": 1, "b": 2, "c": 2},
        "diff":  {},
        "sum":   {"a": 5, "b": 4, "c": 5}},
}

ALL_CASES = MULTISET_CASES + MULTISET_EDGE_CASES


def nonzero(multiset):
    #The multiset as {name: count}, leaving out zero counts.
    return {name: count for name, count in multiset.to_pairs() if count > 0}


class TestHandWorkedResults(unittest.TestCase):
    def test_every_operation_matches_hand_work(self):
        for case in ALL_CASES:
            with self.subTest(case=case["name"]):
                a, b = MultiSet.from_counts(case["A"]), MultiSet.from_counts(case["B"])
                want = EXPECTED[case["name"]]
                self.assertEqual(nonzero(a.union(b)), want["union"])
                self.assertEqual(nonzero(a.intersection(b)), want["inter"])
                self.assertEqual(nonzero(a.difference(b)), want["diff"])
                self.assertEqual(nonzero(a.sum(b)), want["sum"])


class TestAgainstCounter(unittest.TestCase):
    #Independent cross-check: Counter's | & - + are max, min, truncated -, sum.

    def test_matches_counter_operations(self):
        for case in ALL_CASES:
            with self.subTest(case=case["name"]):
                a, b = MultiSet.from_counts(case["A"]), MultiSet.from_counts(case["B"])
                ca, cb = Counter(case["A"]), Counter(case["B"])
                self.assertEqual(nonzero(a.union(b)), dict(ca | cb))
                self.assertEqual(nonzero(a.intersection(b)), dict(ca & cb))
                self.assertEqual(nonzero(a.difference(b)), dict(ca - cb))
                self.assertEqual(nonzero(a.sum(b)), dict(ca + cb))


class TestAssignmentRequirements(unittest.TestCase):
    def test_both_multisets_have_two_counts_above_one(self):
        for case in ALL_CASES:
            with self.subTest(case=case["name"]):
                for side in ("A", "B"):
                    big = [c for c in case[side].values() if c > 1]
                    self.assertGreaterEqual(len(big), 2, f"{side} needs 2+ counts above 1")

    def test_difference_never_negative(self):
        for case in ALL_CASES:
            a, b = MultiSet.from_counts(case["A"]), MultiSet.from_counts(case["B"])
            for result in (a.difference(b), b.difference(a)):
                self.assertTrue(all(c >= 0 for c in result.counts))

    def test_difference_clamps_at_zero(self):
        a, b = MultiSet.from_counts({"a": 2}), MultiSet.from_counts({"a": 5})
        self.assertEqual(a.difference(b).count_of("a"), 0)
        self.assertEqual(b.difference(a).count_of("a"), 3)


class TestEdgeCasesAndProperties(unittest.TestCase):
    def test_difference_with_itself_is_all_zero(self):
        a = MultiSet.from_counts({"a": 3, "b": 2})
        self.assertEqual(a.difference(a), MultiSet.from_counts({}))

    def test_zero_count_in_both_stays_zero(self):
        a, b = MultiSet.from_counts({"a": 1}), MultiSet.from_counts({"b": 1})
        for result in (a.union(b), a.intersection(b), a.difference(b), a.sum(b)):
            self.assertEqual(result.count_of("j"), 0)

    def test_operations_do_not_modify_their_inputs(self):
        a, b = MultiSet.from_counts({"a": 3, "b": 2}), MultiSet.from_counts({"a": 1, "c": 4})
        before = (a.counts, b.counts)
        a.union(b); a.intersection(b); a.difference(b); a.sum(b)
        self.assertEqual((a.counts, b.counts), before)


class TestInvalidInput(unittest.TestCase):
    def test_negative_count_rejected(self):
        with self.assertRaises(ValueError):
            MultiSet.from_counts({"a": -1})

    def test_non_integer_counts_rejected(self):
        for bad in (1.5, "2", None, True):
            with self.subTest(value=bad), self.assertRaises(ValueError):
                MultiSet.from_counts({"a": bad})

    def test_wrong_length_rejected(self):
        with self.assertRaises(ValueError):
            MultiSet([1, 2, 3])

    def test_unknown_element_rejected(self):
        with self.assertRaises(ValueError):
            MultiSet.from_counts({"z": 1})

    def test_operating_on_non_multiset_rejected(self):
        with self.assertRaises(TypeError):
            MultiSet.from_counts({"a": 1}).union({"a": 1})


if __name__ == "__main__":
    unittest.main()