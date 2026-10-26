# Team name: Group 3
# Team members: Erich Mundt, Addie Hurst
# Course and section: CS 2430, section 502
# Project name: Programming Project 2
# File: data.py - hard-coded inputs shared by main.py and tests/.
# Data only, no logic. Part 2 (multiset) data gets added below later.

from Universe import UNIVERSE  # the universe itself is owned by universe.py

# Part 1: ordinary sets (element-name lists)
SET_CASES = [
    {"name": "overlapping",
     "A": ["a", "b", "c", "d", "e"], "B": ["d", "e", "f", "g"]},
    {"name": "disjoint",
     "A": ["a", "b", "c"], "B": ["f", "g", "h"]},
    {"name": "A is a subset of B",
     "A": ["b", "c"], "B": ["a", "b", "c", "d"]},
]

SET_EDGE_CASES = [
    {"name": "edge: A is the empty set",
     "A": [], "B": ["a", "c", "e"]},
    {"name": "edge: A is the full universe",
     "A": list(UNIVERSE), "B": ["a", "c", "e"]},
    {"name": "edge: A equals B",
     "A": ["b", "d", "f"], "B": ["b", "d", "f"]},
]

# ---- Part 2: multisets ({element name: count}; unlisted = 0) ----
# Every case gives BOTH A and B at least two elements with count > 1.
MULTISET_CASES = [
    {"name": "overlapping counts",
     "A": {"a": 3, "b": 2, "c": 1, "e": 4},
     "B": {"a": 1, "b": 5, "d": 2, "e": 2}},
    {"name": "elements only in one multiset",
     "A": {"a": 2, "b": 3},
     "B": {"c": 2, "d": 4}},
    {"name": "identical multisets",
     "A": {"a": 2, "c": 3, "f": 1},
     "B": {"a": 2, "c": 3, "f": 1}},
]

MULTISET_EDGE_CASES = [
    {"name": "edge: B counts exceed A (difference clamps at 0)",
     "A": {"a": 1, "b": 2, "c": 2},
     "B": {"a": 4, "b": 2, "c": 3}},
]

# ---- Change Request: fuzzy sets ({element name: degree}; unlisted = 0.0) ----
FUZZY_CASES = [
    # a: in both | b: only in A | d: only in B | e..j: in neither
    {"name": "intermediate degrees",
     "A": {"a": 0.7, "b": 0.2, "c": 1.0},
     "B": {"a": 0.4, "c": 0.5, "d": 0.9}},
    # exercises the exact boundary degrees 0.0 and 1.0
    {"name": "boundary degrees 0.0 and 1.0",
     "A": {"a": 1.0, "b": 0.0, "c": 0.5},
     "B": {"a": 0.0, "b": 1.0, "c": 0.5}},
]

FUZZY_EDGE_CASES = [
    {"name": "edge: A has no entries (complement is all 1.0)",
     "A": {}, "B": {"a": 0.25}},
    {"name": "edge: A equals B",
     "A": {"a": 0.6, "b": 0.1}, "B": {"a": 0.6, "b": 0.1}},
]
