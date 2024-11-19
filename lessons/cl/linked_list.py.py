from __future__ import annotations


# Notes
#   to get terminal control, option tilda
#   USE DEBUGGER!!
class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    # called when object is being innitilaed for first time

    def __str__(self) -> str:
        """Produced string representation of a linked list return"""
        # return "TODO"
        rest: str = "TODO"
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"

    # looks at the aruments are calls object's str method
    # called automatiacally on any object
    # called wehn obejct is ebing converted to a string


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))
print(one)
print(two)
print(courses)
# make sure to get back here!


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str"""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


print(to_str(one))
print(to_str(two))


def last(head: Node) -> int:
    # saying head is a Node so one, two, courses: when called just in head will continallu go through only that no progress``
    """Return the last value of a non-empty list"""
    # Base Case: wen head is last Node
    #   return its value!
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

    # Recursive case:
    #   Figure out tha last node (recusrive call)
    #   in the rest of the list
    #   return this code


# ****ALWAYS PROGRESS TOWARDS BASE CASE****

# what is simplest way to answer - base case

# print(last(two))  # except 2 - is out base case
# print(last(one))  # ecept to print 2
print(last(courses))  # expect to print 301


# Recursive range fucntion to get recusrive Node list!!!
def recursive_range(start: int, end: int) -> Node | None:
    """build a lost of recursivley from start to end."""

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


a_list: Node | None = recursive_range(110, 113)
print(a_list)
# 2. Try establishing a variable addigned recusssive_range(110,113)
# 3. Tyr printing this variable
