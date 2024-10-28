"""EX06"""

__author__ = "730641436"

# start of code


def invert(invr: dict[str, str]) -> dict[str, str]:  # function definition
    # create an empty dictionary to store inverted valeus
    invrt_dict: dict[str, str] = {}
    for key in invr:  # for in loop
        if invr[key] in invrt_dict:
            # if the vlaue for d[key] in the dictiory d is in invert_dict
            raise KeyError("KeyError")  # is so raise an error
        # can't have more than one same key in dictionary
        invrt_dict[invr[key]] = key
        # else will sdo this which is have the key be the value at d[key] and value will be the key
    return invrt_dict  # returns key


def favorite_color(col: dict[str, str]) -> str:  # function definition
    colors: list[str] = []  # empty list to store colors
    max: int = 0  # to store max number
    new_color: str = ""  # the new max color
    color_count: dict[str, int] = {}
    # empty dictiornary to store the values for numebr of times a color comes up in original dictorianry col
    for key in col:  # for the keys in the dictionary cols
        colors.append(col[key])  # appending the values (colors) from each person's name
    for color in colors:  # now looking at the list with colors
        if color not in color_count:
            # if the color is not in the dictionary that stores the counts for each color
            color_count[color] = 1
            # give that color value 1 and add to dictionary
        if color in color_count:
            # now sees that color is in the dictionary and adds another value to indicate one more instance of thhat color
            color_count[color] += 1
    for color2 in color_count:
        # new value color2 to see the max value in that dictionary of colors and numbers
        if color_count[color2] > max:
            # if the number at that color is greater than the max value, it will replace the max value
            max = color_count[color2]
            new_color = color2
            # thus then the new_color for new max color will become that color2 key value
    return new_color
    # returns the max color new_color variable


def count(l: list[str]) -> dict[str, int]:
    empty: dict[str, int] = {}
    # create an empty dict to store the words and number of times it appears
    for word in l:
        if word in empty:
            # if the word is in the dict empty (litterates thro it)
            empty[word] += 1
            # adds on 1 to value of word in empty b/c its there
        else:
            empty[word] = 1
            # else creates a new key and value with 1 b/c first apperance of word
    return empty
    # returns that dictionary


def alphabetizer(lst: list[str]) -> dict[str, list[str]]:
    lets_wrds: dict[str, list[str]] = {}
    # create an empty list to store new keys and valeus
    for word in lst:  # for loop to itterate over the list which has the words
        if word[0].lower() in lets_wrds:
            # checking if word at index 0 in lower case is in the empty dict
            lets_wrds[word[0].lower()].append(word)
            # is so uses the empty dictionary with the key value of that lower case word and appends that word to that key with that list attached to it

        else:
            lets_wrds[word[0].lower()] = []
            # if not in the empty dictionary, then creates an empty list
            lets_wrds[word[0].lower()].append(word)
            # Then takes that empty list and appends the word to that list

    return lets_wrds


def update_attendance(
    attend_log: dict[str, list[str]], day_of_wk: str, stdnt: str
) -> None:  # function definition
    if day_of_wk in attend_log and stdnt not in attend_log[day_of_wk]:
        # if the day of the week is in the attend_log and the student is not in the attend_log at that day of the week then we want to append that student's name to te day of the week
        attend_log[day_of_wk].append(stdnt)
        # appending the day of the week with the student
    else:  # if above is not true
        attend_log[day_of_wk] = [stdnt]
        # want to replace the day_of_wk value with the new student value complelty to avoid any duplicates in the fucntion
    return  # to exit the function complelty
