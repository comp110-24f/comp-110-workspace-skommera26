"""Mutating functions"""

__author__ = 730651436


def manual_append(a: list[int], num: int) -> None:
    a.append(num)  # appends the lsit by adding num to list


def double(a: list[int]) -> None:
    index: int = 0
    while index < len(a):
        a[index] = a[index] * 2
        index += 1


# itterates over every variable in list to multiply by two per item in list as long as index is smaller than length

list1: list[int] = [1, 2, 3]
list2: list[int] = list1

double(list2) 
# will not print anything b/c no return and because we have no print staemtens in the fucntion bodies
print(list1)
print(list2)
# this print both [2,4,6] b/c sicne the print is under the double functions, it takes into account of double and prints those values
