# Team name: Group 3
# Team members: Erich Mundt, Addie Hurst
# Course and section: CS 2430, section 502
# Project name: Programming Project 2
# Primary author: Erich (Addie provided some additions)
# File: formatting.py - shared output formatting and labels (shared core).
#
# Works with ANY object that has to_bit_string() and to_names(), so it does not
# import the set classes. Labels are defined once, here. Part 2 and the Week 2
# Change Request should add their own label constants in this file.

from Universe import UNIVERSE

SET_LABEL = "[SET]"  # ordinary sets (Part 1)

#multisets (Part 2)
MULTISET_LABEL = "[MULTISET]" 


def format_names(names):
    #Readable element listing, e.g. {a, c, e}; the empty set shows as {}.
    return "{" + ", ".join(names) + "}"


def format_universe():
    #One line documenting the fixed ordering of the universal set.
    pairs = ", ".join(f"{i}:{name}" for i, name in enumerate(UNIVERSE))
    return f"Universe order (index 0 = leftmost bit): {pairs}"


def format_set(title, result):
    #Show a set with BOTH required representations, labeled [SET].
    names = result.to_names()
    listing = format_names(names) + ("  (empty set)" if not names else "")
    return (f"{SET_LABEL} {title}\n"
            f"    bit string : {result.to_bit_string()}\n"
            f"    elements   : {listing}")

#Formats and labels the results of multiset operations.
def format_multiset(title, result):
    #Retrieves the element counts from the MultiSet object.
    counts = result._counts
    #Returns the operation name and its corresponding counts.
    return (f"{MULTISET_LABEL} {title}\n"
            f"    counts: {counts}")
