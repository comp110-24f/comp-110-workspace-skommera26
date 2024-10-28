"""Summing the elements of a list using different loops"""

__author__ = 730651436


def w_sum(vals: list[float]) -> float:
    # uses while loop to iterate over every value in w_sum function
    sum: float = 0.0
    # keeps track of the summations
    index: int = 0
    # need index and sum variable
    while index < len(vals):
        # while loop statement
        sum = sum + vals[index]
        index += 1
    return sum
    # returns sum


def f_sum(vals2: list[float]) -> float:
    # uses for loop to do same thing as w_sum
    sum2: float = 0.0
    for num in vals2:  # condenses the while loop
        sum2 = sum2 + num  # need a sum variable to keep track of the sums
    return sum2
    # returns sum2


def f_range_sum(vals3: list[float]) -> float:  # uses for loop and range
    sum3: float = 0.0
    for idx in range(0, len(vals3)):
        # uses the idx variable to index at a certain value in list
        # gives a number not a word
        sum3 = vals3[idx] + sum3
        # use idx to index over list
    return sum3
    # returns sum3
