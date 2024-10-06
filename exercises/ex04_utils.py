"""list utility functions"""

__author__: str = "730641436"


# start of code!


# first function: itterates through code to see if all integers in list are the same
def all(same_int: list[int], num: int) -> bool:
    """takes list and sees if num is equal to all in the list"""
    index: int = 0
    if len(same_int) == 0:
        # will return False is the elngthj is 0, and will not enter the wile loop
        return False
    while index < len(same_int):
        if same_int[index] != num:
            return False  # sees the return and immedialty exits the function --> does not go to while loop, must exits
        else:
            index += 1  # if equal goes here and index += 1
    return True  # if all indexes are done, and True, then comes here to return True as the final statement


# second function that sees is an empty list or not, and if not then returns the max value of that list
def max(input: list[int]) -> int:
    """finds the maximum number in the list"""
    index1: int = 0
    num1: int = input[index1]  # this will keep track of the max number,
    # and will change if new max number is found
    # num one starts with the first index of the list
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    # this above will be done if python sees list if empty
    else:  # else == false or inital condition not true so goes here
        while index1 < len(input):  # the while statement
            if input[index1] >= num1:  # in input at that index is greater than num1
                # then num1 one will be replaced with that new number
                num1 = input[index1]
            index1 += 1  # then if so it will addmonto index and conitnue itteratiing
        return num1  # at end it will return num1


# second function that takes two lists and sees if each parameter is equal to one anotehr in the list
def is_equal(equal_list1: list[int], equal_list2: list[int]) -> bool:
    """Sees if numbers in equal_lis1 are equal to those in equal_list2"""
    index2: int = 0  # need index to ittterate through list
    if len(equal_list1) != len(equal_list2):
        return False
    while index2 < len(equal_list1):  # while loop intial condition
        if len(equal_list1) != len(equal_list2):
            # makes sure if lens are equal or not
            return False  # is not  = False
        if equal_list1[index2] == equal_list2[index2]:
            # if both indexes are equal it will add onto index
            index2 += 1  # adds onto index to prevent infinite loops
        else:
            return False  # if not no need to contunie so it will return False
    return True  # Now this line won't proceed if False becasue that False statement is in different indentation
    # Oncr while loop is done, and not False, it will come here and return True


# third function that extends the length of first list by adding on the second list
def extend(a: list[int], b: list[int]) -> None:  # no return value
    index3: int = 0
    # index to itterate through the list to add on each index to the new list
    while index3 < len(b):  # while statement
        a.append(b[index3])  # will use the append function to
        # add on the index3 in b to a to create new extended list
        index3 += 1  # add onto the index so it doesn't result in infinte loop
        # no return statement needed
        # when called it will print out a
