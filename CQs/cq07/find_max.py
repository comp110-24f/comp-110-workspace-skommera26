"""Challenge Question 07!"""

__author__ = 730651436


def find_and_remove_max(a: list[int]) -> int:
    idx1: int = 0
    idx2: int = 0
    max: int = 0
    if len(a) == 0:
        return -1

    while idx1 < len(a):
        if a[idx1] >= max:  # checks max values
            max = a[idx1]
            idx1 += 1
        else:
            idx1 += 1

    while idx2 < len(a):
        if max == a[idx2]:
            a.pop(idx2)
            # no need for indexing you just need a value b/c pop doesn't take that in
        else:
            idx2 += 1
    return max
    # put return max at bottom b/c if it beginning it will return max way too ealry
