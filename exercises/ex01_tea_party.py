"""Planing a Tea Party"""

__author__: str = "730641436"


# start of the code!


def main_planner(
    guests: int,
) -> (
    None
):  # return value is none because there is no need for a return value since it is the main function
    """""helps bring all functions togther""" ""
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", tea_bags(people=guests))
    print("Treats:", treats(people=guests))
    print(
        "Cost:", "$" + str(cost(tea_bags(people=guests), treats(people=guests)))
    )  # for the last print statement, have to put in cs=ost function with comma and the cost functin will still interpret the variables as tea_count and tea_bag


# This is the main code, it helps bring all the functions togther in a sense to have them run, and it is the starting point for the code to run


def tea_bags(people: int) -> int:  # returns an integer
    """number of guest attending party so each guest has tea bags"""
    return people * 2


# This is the tea_bags code which helps compute how many people are attending the party


def treats(people: int) -> int:  # also returns an integer
    """number of treats per guest"""
    return int(
        tea_bags(people=people) * 1.5
    )  # put int in front of this to ensure an int is being formed


# This is the treats function which uses the output of the tea bags function to get the number of treats per person


def cost(tea_count: int, treat_count: int) -> float:
    """This helps compute the cost of everything"""
    return ((tea_count) * 0.50) + (
        (treat_count) * 0.75
    )  # don't have to say people=tea_count, cuz then it is as if you are doing the math twice, just say tea count of times 0.5, and the value will be assigned in the main function.


# float times float is auomatically equal to flot so no need to put float in from of return values.
# This is the cost function which computes the cost of everything; it takes the values needed from the main function and puts onto here to compute the cost


if (
    __name__ == "__main__"
):  # This is the main function as well helping give an input to one may put how many guests are attending said party
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
"""this gives an input telling person to give amount if guests and outputs the function"""
# when doing inout functions make sure to put input("") and go from there
# have to put int in front of input because tthe number of guests has to be an int to help evuluate the other functions
