#Project 2: Set Operations
#CS 2430
#Team 3: Addie Hurst, Erich Mundt
#Primary author for this file: Addie Hurst

from Universe import UNIVERSE, index_of
from Validation import require_counts


#Creates class MultiSet
class MultiSet:
    #Constructor using parameters self and counts
    def __init__(self, counts):
        #Check that the counts are valid
        require_counts(counts)
        #Store the list of multiplicities inside the object
        self._counts = tuple(counts)

    #Multiset union: takes the maximum count of each element
    def union(self, other):
        if not isinstance(other, MultiSet):
            raise TypeError("Multiset operations require two MultiSet objects")
        result = []
        #Pairs the corresponding values from both lists
        for a, b in zip(self._counts, other._counts):
            result.append(max(a, b))
        return MultiSet(result)

    @classmethod
    def from_counts(cls, entries):
        #Build from {element name: count}; unlisted elements get count 0.
        counts = [0] * len(UNIVERSE)
        for name, count in entries.items():
            counts[index_of(name)] = count       # ValueError if the name is unknown
        return cls(counts)

    # Multiset intersection: takes the minimum count of each element
    def intersection(self, other):
        if not isinstance(other, MultiSet):
            raise TypeError("Multiset operations require two MultiSet objects")
        result = []
        for a, b in zip(self._counts, other._counts):
            result.append(min(a, b))
        return MultiSet(result)

    #Multiset difference: subtracts counts (without going below zero)
    def difference(self, other):
        if not isinstance(other, MultiSet):
            raise TypeError("Multiset operations require two MultiSet objects")
        result = []
        for a, b in zip(self._counts, other._counts):
            result.append(max(0, a - b))
        return MultiSet(result)
        
    #Multiset sum: adds the counts of the corresponding elements.
    def sum(self, other):
        if not isinstance(other, MultiSet):
            raise TypeError("Multiset operations require two MultiSet objects")
        result = []
        for a, b in zip (self._counts, other._counts):
            result.append(a + b)
        return MultiSet(result)

    #ADDED: public read-only views (Formatting uses these)
    @property
    def counts(self):
        return tuple(self._counts)

    def count_of(self, name):
        return self._counts[index_of(name)]

    def to_pairs(self):
        return list(zip(UNIVERSE, self._counts))

    #ADDED: lets two multisets be compared with ==
    def __eq__(self, other):
        return isinstance(other, MultiSet) and self._counts == other._counts

    def __repr__(self):
        return f"MultiSet({tuple(self._counts)})"