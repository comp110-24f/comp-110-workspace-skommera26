"""EX08."""

from __future__ import annotations


# Class: 11/13/2024


class Node:
    """Above is class definition."""

    # these are the objects of the class
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initialization of the objetcs."""
        self.value = value
        self.next = next
        # innitilaizing the objects - called when innitilzlaed for first time

    def __str__(self) -> str:
        """Produced string representation of a linked list return."""
        # return "TODO"
        rest: str = "TODO"
        # looks at the aruments are calls object's str method
        if self.next is None:
            rest = "None"
        else:
            # called automatiacally on any object
            rest = str(self.next)
        return f"{self.value} -> {rest}"


# called wehn obejct is ebing converted to a string


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))
print(one)
print(two)
print(courses)
# make sure to get back here!


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


# This takes in head and returns the values as a list in string form


print(to_str(one))
print(to_str(two))


def last(head: Node) -> int:
    # saying head is a Node so one, two, courses: when called just in head will continallu go through only that no progress``
    """Return the last value of a non-empty list."""
    print(f"Enter last{head.value}")
    if head.next is None:
        print(f"Return base case: {head.value}")
        return head.value
        # when head is None, it has the last value associalted with it
        # 1 -> 2 -> None ---- see taht 2 is the last value which is assocaited with None
    else:
        # recursive case
        rest: int = last(head.next)  # asking for rest of the list
        # do not say last(head) b/c we are continually adding frames to stack, so there is infinite recurssion
        # head.next is using the next ndoe in the lsit
        print(f"Return recur: {head.value} -> {rest}")
        return rest
    # this helps store thos rest in mempery to be used for the next node


# ****ALWAYS PROGRESS TOWARDS BASE CASE****
print(last(courses))  # expect to print 301


# Class: 11/15/2024
# Recursive range fucntion to get recusrive Node list!!!
def recursive_range(start: int, end: int) -> Node | None:
    """Build a lost of recursivley from start to end."""
    # TODO: can you handle an edge case? what is it?
    # Edge Case
    if start > end:
        raise ValueError("End is greater than the start point")
        # this would be an infinite loop is start is greater than end

    # Reporduce what we wrote by hand here
    if start == end:
        return None
    else:
        # 1. handle the first value in your new list here
        first: int = start
        # 2. let the rest of the lost be handled recusrivly
        rest: Node | None = recursive_range(start + 1, end)
        # 3. reuturn a new node which is followed by the rest
        return Node(first, rest)


a_list: Node | None = recursive_range(110, 120)
print(a_list)


# EXCERSISE CODE

"""Excersise Code starts here."""


# EXERCISE FUNCTION 1
def value_at(head: Node | None, index: int) -> int:
    """This gets the value at a specific value at a specific index for the head argument."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    # Why do we do this when head is None??
    if index == 0:
        return head.value
    # why do we have the index be zero in the sense that like how does it know the indexes to filter through?
    else:
        return value_at(head.next, index - 1)


# EXCERSIE FUNCTION 2
def max(head: Node | None) -> int:
    """This will give the max value for a specifc head argument."""
    if head is None:
        # Base case where if head is already given as None, we need ro raise an error saying we can't call the function with None
        raise ValueError("Cannot call max with None")
    # head is the argument that is in the function where if that value is None; will be ignored if head is None
    if head.next is None:
        return head.value  # if cond is None:
    # Another base case for the fact of if given head = Node (30,None) then will return the value instead of recursing through it
    new_max_value: int = max(head.next)
    # need to have new_max_value as the recursive calling function because if it is just equal to 0, when it goes through the function, it will then recurse through with the new_max_vlaue always being 0 and never changing.
    if head.value > new_max_value:
        return (
            head.value
        )  # return value for head.value when its greater than the new_max_vlaue at that head
    # then it will use that returend value to be added in the frame above to then compare to other values as well
    else:
        return new_max_value
    # if its not greater, then that return value will be the new_max_value and will be used to comapre at other frames (the frame above in this case)


# EXCERSISE FUNCTION 3
def linkify(items: list[int]) -> Node | None:
    """This will linkify or make a link of all the values of an item in a list."""
    if len(items) == 0:
        # edge case: if the length of items is 0, return None
        return None
    else:  # recursive case
        # this takes in the recursive part thet calls ndoe for every element in the list with the [ : ] function
        rest: Node | None = linkify(items[1:])
        # remeber the splicing notation takes the first index, if it takes the 0th indext it will continually call that 0th indext multiple times and will no progress towards that base case sinc the 0th index will be the same
        # first index will keep changing
        return Node(items[0], rest)
    # reutrns the this by calling the Node class onto these functions.


# EXCERISE FUNCTION 4
def scale(head: Node | None, factor: int) -> Node | None:
    """This will scale the head to a specific facotor."""
    # no creat4e a variable where the head is a copy of the Nodes from likify b/c that would still be modifying that list
    if head is None:
        # Base case that says if head is None, will return None without multiplying by factor
        return None
    # Don't want to say head is 0, becasue in Linkify, it wil automatically translate 0 to None
    else:
        start: int = head.value
        # creating a variable where it is an int and is equal to the head.value of that head called in the recursive statement
        start *= factor
        # multiplying the start by a factor
        recurssive: Node | None = scale(head.next, factor)
        # above: recusssive will be the recurvie statement with the head.next which will continually go through the Nodes in Linkify and create new Nodes ratehr than modify it
    # this return statement will take the head which is recursive, and times by factor and return
    return Node(start, recurssive)
    # essentilly will loop through until it reaches None
    # As it loops through, it will multiply each value for head by the factor
