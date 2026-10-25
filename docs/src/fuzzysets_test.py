# Team name: Group 3
# Team members: Erich Mundt, Addie Hurst
# Course and section: CS 2430, section 502
# Project name: Programming Project 2
# Primary author:
# File: tests/test_fuzzy_sets.py - verification for the fuzzy-set Change Request.
# Run from the project root:  python -m unittest -v
#
# FLOATING-POINT TOLERANCE: results are compared within TOLERANCE = 1e-9
# (defined in Fuzzy_sets.py), because 1.0 - 0.7 is 0.30000000000000004, not 0.3.
#
# Checks: (1) hand-worked expected degrees, (2) the change order's own example,
# (3) elements in both / one / neither set, (4) an independent per-element
# formula cross-check, (5) invalid input, (6) mathematical properties.

import math
import unittest

from Data import FUZZY_CASES, FUZZY_EDGE_CASES
from fuzzysets import FuzzySet, TOLERANCE
from Universe import UNIVERSE


def sparse(mapping):
    #Expected set where every unlisted element is 0.0.
    return FuzzySet.from_degrees(mapping)


def mostly_one(mapping):
    #Expected set where every unlisted element is 1.0 (used for complements).
    degrees = {name: 1.0 for name in UNIVERSE}
    degrees.update(mapping)
    return FuzzySet.from_degrees(degrees)


# Expected results worked out by hand (A, B as in Data.py).
EXPECTED = {
    "intermediate degrees": {
        "not_a": mostly_one({"a": 0.3, "b": 0.8, "c": 0.0}),
        "union": sparse({"a": 0.7, "b": 0.2, "c": 1.0, "d": 0.9}),
        "inter": sparse({"a": 0.4, "c": 0.5})},
    "boundary degrees 0.0 and 1.0": {
        "not_a": mostly_one({"a": 0.0, "b": 1.0, "c": 0.5}),
        "union": sparse({"a": 1.0, "b": 1.0, "c": 0.5}),
        "inter": sparse({"c": 0.5})},
    "edge: A has no entries (complement is all 1.0)": {
        "not_a": mostly_one({}),
        "union": sparse({"a": 0.25}),
        "inter": sparse({})},
    "edge: A equals B": {
        "not_a": mostly_one({"a": 0.4, "b": 0.9}),
        "union": sparse({"a": 0.6, "b": 0.1}),
        "inter": sparse({"a": 0.6, "b": 0.1})},
}

ALL_CASES = FUZZY_CASES + FUZZY_EDGE_CASES


class FuzzyTestCase(unittest.TestCase):
    def assertFuzzyClose(self, actual, expected):
        #Compare two fuzzy sets element by element within TOLERANCE.
        for name in UNIVERSE:
            self.assertAlmostEqual(actual.degree_of(name), expected.degree_of(name),
                                   delta=TOLERANCE, msg=f"element '{name}'")


class TestHandWorkedResults(FuzzyTestCase):
    def test_every_operation_matches_hand_work(self):
        for case in ALL_CASES:
            with self.subTest(case=case["name"]):
                a = FuzzySet.from_degrees(case["A"])
                b = FuzzySet.from_degrees(case["B"])
                want = EXPECTED[case["name"]]
                self.assertFuzzyClose(a.complement(), want["not_a"])
                self.assertFuzzyClose(a.union(b), want["union"])
                self.assertFuzzyClose(a.intersection(b), want["inter"])

    def test_change_order_example(self):
        # From the change order: A(x)=0.70, B(x)=0.40
        a, b = FuzzySet.from_degrees({"a": 0.70}), FuzzySet.from_degrees({"a": 0.40})
        self.assertAlmostEqual(a.complement().degree_of("a"), 0.30, delta=TOLERANCE)
        self.assertAlmostEqual(a.union(b).degree_of("a"), 0.70, delta=TOLERANCE)
        self.assertAlmostEqual(a.intersection(b).degree_of("a"), 0.40, delta=TOLERANCE)

    def test_complement_example_with_missing_entry(self):
        # From the change order: y has no stored entry, so complement(y) = 1.0
        a = FuzzySet.from_degrees({"a": 0.70})          # "b" has no entry
        self.assertAlmostEqual(a.complement().degree_of("a"), 0.30, delta=TOLERANCE)
        self.assertAlmostEqual(a.complement().degree_of("b"), 1.00, delta=TOLERANCE)


class TestElementPositions(FuzzyTestCase):
    #Elements in both sets, in only one set, and in neither (but inside U).

    def setUp(self):
        self.a = FuzzySet.from_degrees({"a": 0.7, "b": 0.2})   # b only in A
        self.b = FuzzySet.from_degrees({"a": 0.4, "d": 0.9})   # d only in B

    def test_in_both(self):
        self.assertAlmostEqual(self.a.union(self.b).degree_of("a"), 0.7, delta=TOLERANCE)
        self.assertAlmostEqual(self.a.intersection(self.b).degree_of("a"), 0.4, delta=TOLERANCE)

    def test_only_in_one(self):
        self.assertAlmostEqual(self.a.union(self.b).degree_of("b"), 0.2, delta=TOLERANCE)
        self.assertAlmostEqual(self.a.intersection(self.b).degree_of("b"), 0.0, delta=TOLERANCE)
        self.assertAlmostEqual(self.a.union(self.b).degree_of("d"), 0.9, delta=TOLERANCE)

    def test_in_neither(self):
        self.assertEqual(self.a.union(self.b).degree_of("j"), 0.0)
        self.assertEqual(self.a.intersection(self.b).degree_of("j"), 0.0)
        self.assertAlmostEqual(self.a.complement().degree_of("j"), 1.0, delta=TOLERANCE)


class TestAgainstPlainFormulas(FuzzyTestCase):
    #Independent cross-check using the definitions written out directly.

    def test_matches_definitions(self):
        for case in ALL_CASES:
            with self.subTest(case=case["name"]):
                a, b = FuzzySet.from_degrees(case["A"]), FuzzySet.from_degrees(case["B"])
                for name in UNIVERSE:
                    ma, mb = case["A"].get(name, 0.0), case["B"].get(name, 0.0)
                    self.assertAlmostEqual(a.complement().degree_of(name), 1.0 - ma, delta=TOLERANCE)
                    self.assertAlmostEqual(a.union(b).degree_of(name), max(ma, mb), delta=TOLERANCE)
                    self.assertAlmostEqual(a.intersection(b).degree_of(name), min(ma, mb), delta=TOLERANCE)


class TestRetrievalAndStorage(unittest.TestCase):
    def test_degree_of_returns_stored_and_default(self):
        a = FuzzySet.from_degrees({"c": 0.35})
        self.assertEqual(a.degree_of("c"), 0.35)
        self.assertEqual(a.degree_of("d"), 0.0)

    def test_boundary_degrees_accepted(self):
        a = FuzzySet.from_degrees({"a": 0.0, "b": 1.0})
        self.assertEqual((a.degree_of("a"), a.degree_of("b")), (0.0, 1.0))

    def test_integer_degrees_stored_as_floats(self):
        self.assertIsInstance(FuzzySet.from_degrees({"a": 1}).degree_of("a"), float)

    def test_operations_do_not_modify_their_inputs(self):
        a, b = FuzzySet.from_degrees({"a": 0.7}), FuzzySet.from_degrees({"a": 0.4})
        before = (a.memberships, b.memberships)
        a.union(b); a.intersection(b); a.complement()
        self.assertEqual((a.memberships, b.memberships), before)


class TestProperties(FuzzyTestCase):
    def test_double_complement_returns_original(self):
        a = FuzzySet.from_degrees({"a": 0.7, "b": 0.2, "c": 1.0})
        self.assertFuzzyClose(a.complement().complement(), a)

    def test_de_morgan(self):
        a = FuzzySet.from_degrees({"a": 0.7, "b": 0.2, "c": 1.0})
        b = FuzzySet.from_degrees({"a": 0.4, "c": 0.5, "d": 0.9})
        self.assertFuzzyClose(a.union(b).complement(),
                              a.complement().intersection(b.complement()))

    def test_float_tolerance_is_needed(self):
        # Documents WHY a tolerance exists: exact == fails, tolerance passes.
        value = FuzzySet.from_degrees({"a": 0.7}).complement().degree_of("a")
        self.assertNotEqual(value, 0.3)
        self.assertTrue(math.isclose(value, 0.3, abs_tol=TOLERANCE))


class TestInvalidInput(unittest.TestCase):
    def test_degree_above_one_rejected(self):
        with self.assertRaises(ValueError):
            FuzzySet.from_degrees({"a": 1.1})

    def test_degree_below_zero_rejected(self):
        with self.assertRaises(ValueError):
            FuzzySet.from_degrees({"a": -0.1})

    def test_nan_rejected(self):
        with self.assertRaises(ValueError):
            FuzzySet.from_degrees({"a": float("nan")})

    def test_non_numbers_rejected(self):
        for bad in ("0.5", None, True):
            with self.subTest(value=bad), self.assertRaises(ValueError):
                FuzzySet.from_degrees({"a": bad})

    def test_unknown_element_rejected(self):
        with self.assertRaises(ValueError):
            FuzzySet.from_degrees({"z": 0.5})
        with self.assertRaises(ValueError):
            FuzzySet.from_degrees({}).degree_of("z")

    def test_wrong_length_array_rejected(self):
        with self.assertRaises(ValueError):
            FuzzySet([0.5, 0.5])

    def test_operating_on_non_fuzzy_rejected(self):
        with self.assertRaises(TypeError):
            FuzzySet.from_degrees({"a": 0.5}).union({"a": 0.5})


if __name__ == "__main__":
    unittest.main()