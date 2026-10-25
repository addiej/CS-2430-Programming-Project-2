from Validation import require_memberships

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
