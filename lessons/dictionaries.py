"""Examples of dictionary syntax with Ice Cream Shop order tallies"""

ice_cream: dict[str, int] = {"Chocolate": 12, "Vanilla": 8, "Strawberry": 5}
# always have to define the function name with dict[<key word>, <int>]

# len evaluates to number of entries
print(len(ice_cream))  # prints 3

# add key-value entry by directly assigning to a key
ice_cream["mint"] = 3
# to add something to dictionary do in this syntax above
# dict_name[<key value to add>] = <value>

# acesss entries by their key

print(ice_cream["Chocolate"])  # prints 12

# test if "pbj" is a key in ice_cream
has_pbj: bool = "pbj" in ice_cream
# returns false becasue has_pbj is not existant in the dictionary ice_cream
# this is how to test if a value is there in the dictioanry

# removing items from list - use pop and give it a key
ice_cream.pop("Strawberry")
# make sure to keep caps the same since that is import here!

# to loop over every item in dictionary can't use while lopp
# while lopp sequences over a sequence of numbers
# in dictionaries, you want to use a for in loop
for flavor in ice_cream:  # itterates over the keys
    # this itterates over the flavors (keys) in dictionary ice_cream
    tally: int = ice_cream[
        flavor
    ]  # creates a variable called tally to use to then take flavors and index number of ice creams for taht key value
    print(f"{flavor} has {tally} orders")
