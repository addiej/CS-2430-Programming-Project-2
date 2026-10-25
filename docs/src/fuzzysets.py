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
    
