# Team name: Group 3
# Team members: Erich Mundt, Addie Hurst
# Course and section: CS 2430, section 502
# Project name: Programming Project 2
# File: formatting.py - shared output formatting and labels (shared core).
#
# Works with ANY object that has to_bit_string() and to_names(), so it does not
# import the set classes. Labels are defined once, here. Part 2 and the Week 2
# Change Request should add their own label constants in this file.

from Universe import UNIVERSE

SET_LABEL = "[SET]"  # ordinary sets (Part 1)

#multisets (Part 2)
MULTISET_LABEL = "[MULTISET]"

# added for the fuzzy-set Change Request
FUZZY_LABEL = "[FUZZY]"    # fuzzy sets; never mixed with [SET] or [MULTISET]


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
    entries = [f"{name}:{count}" for name, count in result.to_pairs() if count > 0]
    listing = "{" + ", ".join(entries) + "}" if entries else "{}  (empty multiset)"
    return (f"{MULTISET_LABEL} {title}\n"
            f"    counts   : {result.counts}\n"
            f"    elements : {listing}")

def format_fuzzy(title, fuzzy):
    # Shows every non-zero degree with 2 decimals, labeled [FUZZY].
    entries = [f"{name}: {degree:.2f}"
               for name, degree in fuzzy.to_pairs() if degree > 0.0]
    listing = "{" + ", ".join(entries) + "}" if entries else "{}  (all degrees 0.00)"
    return (f"{FUZZY_LABEL} {title}\n"
            f"    degrees : {listing}\n"
            f"    (elements not listed have degree 0.00)")