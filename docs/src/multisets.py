from Universe import UNIVERSE
from Validation import require_counts


#Creates class MultiSet
class MultiSet:
    #Constructor using parameters self and counts
    def __init__(self, counts):
        #Check that the counts are valid
        require_counts(counts)

        #Store the list of multiplicities inside the object
        self._counts = list(counts)

    #Multiset union: takes the maximum count of each element
    def union(self, other):
        if not isinstance(other, MultiSet):
            raise TypeError("Multiset operations require two MultiSet objects")
        result = []
        #Pairs the corresponding values from both lists
        for a, b in zip(self._counts, other._counts):
            result.append(max(a, b))
        return MultiSet(result)

    # Multiset intersection: takes the minimum count of each element
    def intersection(self, other):
        if not isinstance(other, MultiSet):
            raise TypeError("Multiset operations require two MultiSet objects")
        result = []
        for a, b in zip(self._counts, other._counts):
            result.append(min(a, b))
        return MultiSet(result)
