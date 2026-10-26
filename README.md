# CS-2430-Programming-Project-2

# Programming Project 2: Sets, Multisets, and Fuzzy Sets

Team: Group 3 (Erich Mundt, Addie Hurst)
Course: CS 2430, section 502
Language: Python 3 (developed with Python 3.14; no outside packages required)

## What this project does

This program implements three mathematical structures over one fixed universal set
of 10 elements (`a` through `j`):

1. **Ordinary sets (Part 1)**, stored as Boolean arrays / bit strings. Operations:
   complement (NOT A), union, intersection, difference (A - B), and symmetric
   difference.
2. **Multisets (Part 2)**, stored as one non-negative integer count per element.
   Operations: union (max), intersection (min), difference (not below 0), and sum.
3. **Fuzzy sets (Week 2 Change Request)**, stored as one membership degree between
   0.0 and 1.0 per element. Operations: complement (1 - x), union (max),
   and intersection (min).

All output is labeled so the structures are never confused:
`[SET]`, `[MULTISET]`, and `[FUZZY]`.

## How to run

Run these commands from the project root folder (the one containing `Main.py`).

| Task | Command |
|---|---|
| Run all demos (sets, multisets, fuzzy sets) | `python Main.py` |
| Run all tests (sets, multisets and fuzzy) | `python -m unittest -v` |
| Print the fuzzy-set verification report | `python Fuzzy_report.py` |

On some systems the command is `python3` instead of `python`.
The expected test result is `OK` on the last line.

## Project structure


```
Main.py              Runs every demo with labeled output
Data.py              Hard-coded inputs for all demos and tests
Universe.py          The universal set and its fixed order
Validation.py        Shared input checks
Formatting.py        Shared output formatting and labels
Sets_bitstring.py    Part 1: BitSet class
Multisets.py         Part 2: MultiSet class
fuzzysets.py        Change Request: FuzzySet class
fuzzy_report.py      Prints inputs, expected, and actual fuzzy results
Test_sets.py         Unit tests for sets
test_multisets.py.   Unit tests for multisets
fuzzysets_test.py    Unit tests for fuzzy sets
results/             Saved program and test output (evidence)
docs/                Project Plan and design artifacts
CONTRIBUTIONS.md     Who did what, with evidence pointers
```

## Key design decisions

- **Universe ordering:** `Universe.py` defines the order `a b c d e f g h i j`.
  Index 0 is the leftmost bit. Every other module takes element names and positions
  from this file.
- **Shared code:** validation (`Validation.py`) and output formatting
  (`Formatting.py`) are used by every part. The operation modules only compute and
  never print.
- **Immutability:** every operation returns a new object and never changes its
  inputs.

## Fuzzy-set rules (Change Request)

- A membership degree is a number from 0.0 to 1.0, inclusive. It is not a probability.
- An element of the universe with no stored entry has degree 0.0, so its complement
  is 1.0.
- **Invalid input** raises `ValueError`: a degree below 0.0 or above 1.0, NaN,
  a non-number (such as a string or `None`), a boolean, a wrong number of
  degrees, or an element name that is not in the universe.
- **Floating-point tolerance:** results are compared with a tolerance of
  `1e-9` (`TOLERANCE` in `Fuzzy_sets.py`), because floats are inexact
  (for example, `1.0 - 0.7` is `0.30000000000000004`).

## Testing

- Each part has representative cases and at least one edge case (see `Data.py`).
- Multiset test data gives both A and B at least two elements with count above 1.
- Expected results were worked out by hand and are written in the test files.
- After the Change Request, the full suite was rerun to confirm that the original
  set and multiset behavior still works.
