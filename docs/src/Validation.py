# Team name: Group 3
# Team members: Erich Mundt, Addie Hurst
# Course and section: CS 2430, section 502
# Project name: Programming Project 2
# Primary author:
# File: validation.py - shared input checks (shared core; used by Part 1 and,
# later, by Part 2 and any Change Request code).
#
# Each check raises ValueError with a clear message instead of letting bad
# data produce a wrong answer silently.

from Universe import size


def require_bits(bits):
    #Check a bit array has exactly n entries and each entry is True/False (or 0/1).
    if len(bits) != size():
        raise ValueError(
            f"expected {size()} bits (one per universe element), got {len(bits)}")
    for position, value in enumerate(bits):
        if value not in (True, False):  # also accepts 0 and 1
            raise ValueError(
                f"bit {position} must be True/False (or 0/1), got {value!r}")


def require_same_size(first, second):
    #Check two bit-based sets have the same number of positions.
    if len(first.bits) != len(second.bits):
        raise ValueError(
            f"size mismatch: {len(first.bits)} bits vs {len(second.bits)} bits")
#creates a functions which acceptsd a list of multiplicities
def require_counts(counts):
    #check whether the number of items in the list is different from the size of the universal set
    if len(counts) != size():
        #stop operation and reports an error if the list has the wrong number of elements
        raise ValueError("Invalid number of counts")
