"""EX07."""

__author__ = "730641436"

"""File to define Fish class."""


class Fish:
    """Class Fish."""

    # creates a class called Fish
    age: int
    # this is the variable assigned to that class

    def __init__(self):
        """Innit fucntion that takes in self as the parameter - creates new frame and heap id."""
        self.age = 0
        # self.age to show it is its own variable
        return None

    def one_day(self):
        """Function that calculates age per day."""
        # this method also takes in self, and updates seld by adding one
        # this is refernce to self in the heap of memeory
        self.age += 1
        return None
