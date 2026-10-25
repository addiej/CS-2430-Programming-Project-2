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
    self._memberships = list(memberships)

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