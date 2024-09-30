"""Challenge Question 03!"""

__author__ = 730651436


# code starts here
def get_coords(
    xs: str, ys: str
) -> None:  # function signature; has return None and takes in two parameters
    index: int = 0  # index for xs
    index2: int = 0  # index for ys
    while index < len(xs):  # first while loop
        index2 = 0  # need to say this b/c we want the index2 to reset to 0 everytime we come back here for that it can reiterate over the xs loop to print all characters of ys with that character of xs, or else it will not print the other ys variables with the next xs variable since that while loop will not run
        while index2 < len(ys):
            print((xs[index], ys[index2]))  # prints the coordinates
            index2 += 1  # adds one to the index2
        index += 1  # then once this indented while loop is false it will add on to the index for xs
