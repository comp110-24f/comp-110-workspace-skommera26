"""practicing with lists"""

my_numbers: list[float] = []  # empty list w/ literal
my_numbers: list[float] = list()  # constructor - retruns empty list like that

print(my_numbers)
# string analogy
# my_name: str = "" --> literal; --> uses a literal to identify the list
# my_name: str = str() --> constructor --> uses a constructor to identify the list

# adding value to list
my_numbers.append(1.5)
my_numbers.append(2.3)
my_numbers.append(2.3)  # using append methos
# need to add aditional append functions for each value you want to add
# append only allows one value at a time sadly....

print(my_numbers)
# now that its appended, it will print out the 1.0 taht is appended to the list
# notice it divides each vlaue with commoa and square brackets

# create list called game_points that stores the following numbers: 102,86,94
game_points: list[int] = [102, 86, 94]
# creating already populated list (already has numbers)
print(game_points)

# using subscription notation
print(game_points[2])

last_game: int = game_points[2]
# storing 94 and storing as a variable!

# using subscription notation to modify game_points 86.
game_points[1] = 72  # tells to replace 86 with 72
print(game_points)

# example why imprt
# class_num: str = "110" #change to 210; class is keyword in python
# class_num[0] = "2" #can't modify like ints b/c strings are imutable!

# printing out length of game points
print(len(game_points))
# length is 3 b/s there are three objects in the list

# removing a variable
game_points.pop(1)  # index of variable you want to remove
print(game_points)
# will remove 72 b/c index is index 1
# now index is shifted


# PRACTICE
# function name: display; parameters: list of integers; RV: None;
# print every element in the input list
# we want our list integers to be same as game_points


def display(my_num: list[int]) -> None:
    """displays all elements on int list"""
    index: int = 0
    while index < len(my_num):
        print(my_num[index])
        index += 1


display(my_num=game_points)

print(["Kris", "Kaki", "Alyssa"][1])
