"""Challenge Question 03!"""

__author__ = 730651436


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0
    while index < len(
        phrase
    ):  # need an if else statement to show that if the phrase's index is equal to sear_char, then add onto index and add onto count
        if phrase[index] == search_char:
            index += 1
            count += 1
        else:  # the else shows that it will alows add ont index because it needs to go through every variable
            index += 1
    # The while loop helps go through the whole code and whole phrase until its over, and once it is, it goes back to while statment to check if the index is smaller than the length,
    # if length is greater than index, then continues with loop, if not then stops loop and goes to return
    return count
