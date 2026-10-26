# Team name: Group 3
# Team members: Erich Mundt, Addie Hurst
# Course and section: CS 2430, section 502
# Project name: Programming Project 2
# File: Fuzzy_sets.py - Change Request: fuzzy sets.

# A fuzzyset stores one membership degree (a float in [0.0, 1.0]) per element of
# the universe, in the order fixed by Universe.py. 0.0 = not a member, 1.0 = full
# member, anything between = partial member. A degree is NOT a probability.
#
# Like BitSet, this class only COMPUTES: it never prints, and every operation
# returns a NEW object (inputs are never changed).
#
# MISSING ENTRIES: an element of the universe with no stored entry has degree 0.0,
# so complement (which covers EVERY element of the universe) gives it 1.0.
#
# INVALID INPUT: Validation.require_memberships raises ValueError for a wrong
# number of degrees, non-numbers, booleans, NaN, and degrees below 0.0 or above
# 1.0. An element name that is not in the universe also raises ValueError
# (from Universe.index_of).


from Validation import require_memberships
from Universe import UNIVERSE, index_of

# Floating-point results are inexact (1.0 - 0.7 is 0.30000000000000004),
# so results are compared within this small tolerance, never with ==.
TOLERANCE = 1e-9

#Declares class FuzzySets.
class FuzzySet:
  #Constructor that initialises the FuzzySet class with parameters self and memberships. 
  def __init__(self, memberships):
    #Checks whether the input is valid
    require_memberships(memberships)
    #Stores memberships degrees inside the Object.
    self._memberships = tuple(float(m) for m in memberships)

  #Complement of FuzzySet; subtracts each membership degree from 1.0.
  def complement(self):
      result = []
      #Loops through each membership degree and calculates its complement.
      for x in self._memberships:
        result.append(1.0 - x)
      #Returns a new FuzzySet containing the complemented membership degrees.
      return FuzzySet(result)

  #Compares the membership degrees of 2 fuzzy-sets and keeps the larger value for each
  #element.
  def union(self, other):
      if not isinstance(other, FuzzySet):
          raise TypeError("FuzzySet operations require 2 FuzzySet objects")
      result = []
      #Pairs the corresponding values from both lists
      for a, b in zip(self._memberships, other._memberships):
          result.append(max(a, b))
      return FuzzySet(result)
    
  #Compares the membership degrees of 2 fuzzy sets and keeps the smaller value for each element.
  def intersection(self, other):
      if not isinstance(other, FuzzySet):
          raise TypeError("FuzzySet operations require 2 FuzzySet objects")
      result = []
      #Pairs the corresponding values from both lists
      for a, b in zip(self._memberships, other._memberships):
          result.append(min(a, b))
      return FuzzySet(result)

  @classmethod
  def from_degrees(cls, entries):
  #Build from {element name: degree}. Unlisted elements get 0.0.
      memberships = [0.0] * len(UNIVERSE)
      for name, degree in entries.items():
              memberships[index_of(name)] = degree      # ValueError if name unknown
      return cls(memberships)

  def to_pairs(self):
      #Every (element, degree) pair, in universe order (used by formatting).
      return list(zip(UNIVERSE, self._memberships))

  def degree_of(self, name):
      #Retrieve the membership degree of one element."""
      return self._memberships[index_of(name)]

  @property
  def memberships(self):
      return self._memberships