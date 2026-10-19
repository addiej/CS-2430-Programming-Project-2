# Team name: Group 3
# Team members: Erich Mundt
# Course and section: CS 2430, section 502
# Project name: Programming Project 2
# Primary author:
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

# Part 2: Multiset data
MULTISET_A = [3, 2, 1, 0, 2, 0, 0, 0, 0, 0]
MULTISET_B = [1, 4, 2, 0, 1, 0, 0, 0, 0, 0]
