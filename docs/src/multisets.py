from Universe import UNIVERSE


#creates class MultiSet  
class MultiSet:
    #constructor using parameters self and oounts
    def __init__(self, counts):
      #This stores the list of multiplicities inside the object.
      self._counts = list(counts)
    
