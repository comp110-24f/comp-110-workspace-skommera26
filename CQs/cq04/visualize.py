from CQs.cq04.concatenation import (
    concat,
)  # remember format of the folder(package name(may be more than one like here!)).module name import function name from file

x: str = "123"  # global variables
y: str = "abc"  # global variables

print(
    concat(x, y)
)  # calls the concat function and prints it using the global variables assigned here

from CQs.cq04.coordinates import (
    get_coords,
)  # remember format of the folder(package name(may be more than one like here!)).module name import function name from file


print(
    get_coords(x, y)
)  # now uses these global variables to print output of get_coords function with x and y


"""importing coordinate and contact functions"""


__author__ = "730651436"
