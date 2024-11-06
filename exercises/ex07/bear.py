"""EX07."""

__author__ = "730641436"

"""File to define Bear class."""


class Bear:
    """Class Bear."""

    # creates a new class called Bear
    age: int
    # this is the age variable
    hunger_score: int
    # this is the hunger_score variable

    def __init__(self):
        """Innit function that takes in self as a parameter - creates new frame."""
        self.age = 0
        # takes self new way to show age and hunger_score
        self.hunger_score = 0
        return None

    def one_day(self):
        """This uses self to update age and hunger score by day."""
        # uses self which will be a reference in the heap when called and will be updated there
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """This takes in self, and other parameter o update the hunger_score with number of fish."""
        # self will be a reference to the heap in memeory and the num_fish will be assigned
        self.hunger_score += num_fish
        return None
