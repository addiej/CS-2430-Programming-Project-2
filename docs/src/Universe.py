# Group 3
# Team members: Erich Mundt, Addie Hurst
# Course and section: CS 2430, section 502
# Project name: Programming Project 2
# File: Universe.py - the ONE place that defines the universal set and its order.
#
# ORDERING RULE (document this in the report): UNIVERSE[0] is the LEFTMOST bit
# of every bit string. Every other module gets element names and positions
# from here, so changing the universe means editing only this file.

# A tuple so nothing can accidentally change the order at run time.
UNIVERSE = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")  # n = 10


def size():
    #Return n, the number of elements in the universal set.
    return len(UNIVERSE)

def index_of(name):
    #Return the bit position of an element name; ValueError if it is unknown.
    try:
        return UNIVERSE.index(name)
    except ValueError:
        raise ValueError(
            f"'{name}' is not in the universe {list(UNIVERSE)}") from None

def name_at(index):
    #Return the element name stored at a bit position.
    return UNIVERSE[index]