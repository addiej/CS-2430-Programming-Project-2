from Universe import UNIVERSE
from Validation import require_counts


# Creates class MultiSet
class MultiSet:
    # Constructor using parameters self and counts
    def __init__(self, counts):
        # Check that the counts are valid
        require_counts(counts)

        # Store the list of multiplicities inside the object
        self._counts = list(counts)
