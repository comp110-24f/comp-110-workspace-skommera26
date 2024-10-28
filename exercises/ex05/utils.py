"""EX05"""

__author__ = "730641436"

# start of the code!


def only_evens(a: list[int]) -> list[int]:
    new_l: list[int] = []
    # need to assign a variable to global variabels!!
    for num in a:
        # for a number in list a it will itterate thro the lsit
        if num % 2 == 0:
            # ensures it is a even number
            new_l.append(num)
    return new_l  # returns the even list or empty


# for this assert statement can have the calling function


def sub(b: list[int], int1: int, int2: int) -> list[int]:
    if int1 < 0:
        # if the first index is greater than 0, it will make it as 0
        int1 = 0
    if int2 > len(b):
        # if the second index is greater than len(b) it will make it so that it is the len(b)
        int2 = len(b)
    if len(b) == 0 or int1 >= len(b) or int2 <= 0:
        # if len(b) is 0, or the first int is greater than len(b) or sedond int is less than 0, it wil lreturn empty list
        return []
    range_l: list[int] = []
    # identifying the list here that will add elements of b
    for idx in range(int1, int2):
        # for in loop itterating through b
        range_l.append(b[idx])
        # will add the indexes within that range to this new list
    return range_l  # returns rnage


# so if test cases for this you can call function in asser statement becasue it is not returning none rather the range_l list


def add_at_index(c: list[int], add_num: int, chk_idx: int) -> None:
    # returns none, so in test cases you do not have to put asssert call the function, just need to say if the og list equals what you modify it to be
    if chk_idx > len(c) or chk_idx < 0:
        raise IndexError(" Index is out of bounds for the input list")
    # only need to raise an IndexError if the chk_idx is greater than len(c) or if the chk_idx is less than 0
    # if list is empty and adding at index 0, you can still add the number b/c it is not out of range since length 0 has index 0

    if chk_idx == len(c):
        # if the chk_indx is equal to len of list, you just need to append the add number
        c.append(add_num)

    else:  # if anything else then do this
        c.append(0)  # adds on arbritary number
        for idx in range(len(c) - 1, chk_idx, -1):
            # need to say len(c) -1 b/cwe are including that portion so much be that index since len(c) will give index out of range!
            # need to say from the end of list to the chk_idx point, and will subtract one from there b/c we are starting from end and going to from to replace variables in indexes
            c[idx] = c[idx - 1]
            # saying that c at that index is now replaced by the number in index before that

        c[chk_idx] = add_num
        # once done wth the for in loop, it wil lreplace the c[chk_idx] with the add_num variable since there will be empty place for it
