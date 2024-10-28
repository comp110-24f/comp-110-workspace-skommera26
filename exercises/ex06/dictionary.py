"""EX06"""

__author__ = "730641436"

# start of code


def invert(d: dict[str, str]) -> dict[str, str]:
    invrt_dict: dict[str, str] = {}
    for key in d:
        if d[key] in invrt_dict:
            raise KeyError("KeyError")
        invrt_dict[d[key]] = key
    return invrt_dict  # add on value error???


def favorite_color(c: dict[str, str]) -> str:
    colors: list[str] = []
    max: int = 0
    new_color: str = ""
    color_count: dict[str, int] = {}
    for key in c:
        colors.append(c[key])
    for color in colors:
        if color not in color_count:
            color_count[color] = 0
        if color in color_count:
            color_count[color] += 1
    for color2 in color_count:
        if color_count[color2] > max:
            max = color_count[color2]
            new_color = color2
    return new_color


def count(l: list[str]) -> dict[str, int]:
    empty: dict[str, int] = {}
    for word in l:
        if word in empty:
            empty[word] += 1
        else:
            empty[word] = 1
    return empty


def alphabetizer(lst: list[str]) -> dict[str, list[str]]:
    lets_wrds: dict[str, list[str]] = (
        {}
    )  # create an empty list to store new keys and valeus
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
) -> None:
    for day in attend_log:
        if day_of_wk not in attend_log:
            attend_log[day_of_wk] = []
            attend_log[day_of_wk].append(stdnt)
        if day in attend_log:
            attend_log[day_of_wk].append(stdnt)
