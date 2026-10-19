from Universe import UNIVERSE
from Validation import require_counts

#creates class MultiSet  
class MultiSet:
    #constructor using parameters self and oounts
    def __init__(self, counts):
      #This stores the list of multiplicities inside the object.
      self._counts = list(counts)
    
