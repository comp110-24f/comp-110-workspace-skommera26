def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char removed."""
    copy: str = ""  # Set up empty str to copy values over
    index: int = 0
    while index <= len(msg):
        if msg[index] != char:  # if msg{index} != char
            copy += msg[index]
            # need to put msg[index] becasue you want that character ot the character that you put into function!!
        index += 1
        # no neeed for else statement!
    return copy


if __name__ == "__main__":
    # only runs if main is the name
    # remove_chars(msg="footbalpythonl", char="o") -> "ftball"
    # create a variable called word with the value "type"
    word: str = "yoyo"  # GLOBAL variable
    # print the result of calling your function with argument word and "y"
    print(remove_chars(msg=word, char="y"))  # with keyword arugments
    # print the reuslt of calling your function with argu,ents word and "o"
    print(remove_chars(word, "o"))  # with positional arguments
