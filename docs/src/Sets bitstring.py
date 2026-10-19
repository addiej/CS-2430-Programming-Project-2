# Team name: Group 3
# Team members: Erich Mundt, Addie Hurst
# Course and section: CS 2430, section 502
# Project name: Programming Project 2
# Primary author:
# File: sets_bitstring.py - Part 1: ordinary sets stored as Boolean arrays.
#
# A BitSet holds one True/False per universe element, in the order fixed by
# universe.py. True means "this element is in the set".
# This file only COMPUTES. It never prints and never adds output labels;
# formatting.py does that.
# [SET] labels live in one place.

from universe import UNIVERSE, index_of
from validation import require_bits, require_same_size


class BitSet:
    # An ordinary set over UNIVERSE, stored as an immutable Boolean array.

    def __init__(self, bits):
        require_bits(bits)  # right length, only True/False
        self._bits = tuple(bool(b) for b in bits)  # tuple => cannot be modified

    #construction
    @classmethod
    def from_names(cls, names):
        #Build a set from element names, e.g. BitSet.from_names(["a", "c"]).
        bits = [False] * len(UNIVERSE)
        for name in names:
            bits[index_of(name)] = True  # ValueError if name unknown
        return cls(bits)

    # ---------- the five required operations ----------
    def complement(self):
        #NOT(A): flip every bit (everything in the universe that is not in A).
        return BitSet([not b for b in self._bits])

    def union(self, other):
        #A U B: present if in A OR in B.
        return self._combine(other, lambda a, b: a or b)

    def intersection(self, other):
        #A n B: present if in A AND in B.
        return self._combine(other, lambda a, b: a and b)

    def difference(self, other):
        #A - B: present if in A AND NOT in B.
        return self._combine(other, lambda a, b: a and not b)

    def symmetric_difference(self, other):
        #A xor B, built exactly as the assignment defines it: (A - B) U (B - A).
        return self.difference(other).union(other.difference(self))

    # read-only views, no printing here
    @property
    def bits(self):
        #The Boolean array as a tuple.
        return self._bits

    def to_bit_string(self):
        #Display form such as '1100110000' (leftmost = UNIVERSE[0]).
        return "".join("1" if b else "0" for b in self._bits)

    def to_names(self):
        #Element names that are present, in universe order.
        return [UNIVERSE[i] for i, b in enumerate(self._bits) if b]

    def __eq__(self, other):
        return isinstance(other, BitSet) and self._bits == other._bits

    def __repr__(self):
        return f"BitSet('{self.to_bit_string()}')"

    # one shared loop instead of three copies
    def _combine(self, other, rule):
        #Apply `rule` to the two bits at every position, return a new BitSet.
        if not isinstance(other, BitSet):
            raise TypeError("set operations need two BitSet objects")
        require_same_size(self, other)
        return BitSet([rule(a, b) for a, b in zip(self._bits, other._bits)])