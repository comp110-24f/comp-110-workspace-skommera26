"""EX05"""

__author__ = "730641436"

# start of the code!


def only_evens(a: list[int]) -> list[int]:
    new_l: list[int] = []  # need to assign a variable to global variabels!!
    for num in a:  # for a number in list a it will itterate thro the lsit
        if num % 2 == 0:  # ensures it is a even number
            new_l.append(num)
    return new_l  # returns the even list or empty


def sub(b: list[int], int1: int, int2: int) -> list[int]:
    if int1 < 0:
        int1 = 0
    if int2 > len(b):
        int2 = len(b)
    if len(b) == 0 or int1 >= len(b) or int2 <= 0:
        return []
    range_l: list[int] = []
    for idx in range(int1, int2):
        range_l.append(b[idx])
    return range_l


def add_at_index(c: list[int], add_num: int, chk_idx: int) -> None:
    if c == []:
        raise IndexError("Index is out of bounds for the input list")
    if chk_idx == len(c):
        c.append(add_num)

    else:
        c.append(0)
        for idx in range(len(c) - 1, chk_idx, -1):
            c[idx] = c[idx - 1]

        c[chk_idx] = add_num
