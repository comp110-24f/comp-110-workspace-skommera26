pets: list[str] = ["Louie", "Bo", "Bear"]
for var in pets:  # this will be same indentation as the pets list!!
    print(f"Good boy, {var} !")  # can use f string to write this
    # the var is like a variable that takes on speicifc values at a certain index in the list
    # once done, it will loop back to for, until elements are done!
    # can put any element name!
names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, len(names)):
    # this gives us the indexes with the range funmction of each variabe in the list
    print(f"{idx}: {names[idx]}")
    # this will print the range of the list as well, and using the idx numbers will print out the indexes using idx in the list using thr range
