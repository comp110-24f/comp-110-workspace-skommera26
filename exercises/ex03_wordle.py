"""EX03 - Wordle!"""

__author__ = "730641436"


# main fuinction that will add eveyrthing togther
def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    g_bx: str = "\U0001F7E9"  # green box
    turn: int = 1  # turns to keep track of
    boxes: str = ""  # this is to assign whole calling of all functions to
    while turn <= 6:  # initial contiion (we want to be equal to so
        # 6th turn is also accounted for)
        print(f"=== Turn {turn}/6 ===")
        boxes = emojified(input_guess(len(secret)), secret)
        print(boxes)
        # want to asssign a variable b/c if the above statement
        # was w/o variable it would print it twice w/o chacking if true
        if boxes == g_bx * len(secret):
            print(f"You won in {turn}/6 turns!")
            return  # putting return statement helps exit out of the code without exiting out of the terminal complelty
        elif boxes != g_bx * len(secret):
            turn += 1  # this says if the boxes are not all green then add onto the turn
            # we do not need to add onto turn when it is equal becasue it will exit out eitehr way
    print("X/6 - Sorry, try again tomorrow!")
    # this will be printed when the while loop is false or when turns is greater than 6


# start of code
def input_guess(secret_word_len: int) -> str:  # sees if length of
    # secret word is equal to length of word inputted by user
    """takes in the local variable word that is inputted and checks to see if it is the length if secret_word_len!"""
    word: str = input(f"Enter a {secret_word_len} character word: ")
    # need to make word equal to the input so the word that person gives is stored
    while len(word) != secret_word_len:
        # will say not equal to b/c we want this to be true so it enters loop and corrects the person
        if len(word) != secret_word_len:
            # easier to say than two functions for > and <
            word = input(f"That wasn't {secret_word_len} chars! Try again: ")
            # declare the word to be equal to the input so
            # the while loop can go through and function until right len is given
    return word  # will return and store the right word


# second fucntion that itterates through each word to see if true or false by seeing if that letter is present in the sngl_cahr
def contains_char(check_word: str, sngl_char: str) -> bool:
    # reiterates through the word to see if any matches of index of word with snglchar
    """this function takes the word and checks indexes of the word to see if it matches the snlgchar"""
    assert len(sngl_char) == 1  # makes sure that the sngl_char is 1
    # character long
    index: int = 0  # index
    while index < len(check_word):  # initial condition of len being
        # greater than index so error doesn't come up
        if check_word[index] != sngl_char:  # if index of check_wrd not
            # equal to sngl_char, it will add index to check other
            # characters in the word
            index += 1
        elif check_word[index] == sngl_char:
            # need to use elif so it stops after True comes
            # if one of characters in word is equal to sngl_cahr
            # it will return True!
            return True
    return False  # when while loop is false it returns False


# thirds emojii function!
def emojified(guess: str, secret_word: str) -> str:
    """checks secret and guess word to assign emojis to it"""
    assert len(guess) == len(secret_word)  # makes sure the length of guess
    # is the same as the length of secret

    # these are all the emojis used in this code
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index1: int = 0  # only need one index for this b/c the other index
    # for when guess[index1] not equal to secret[index1] it will use the index from contains_cahr to iterate through whole word to see if there is a character present in word in wrong location

    constant: str = ""  # use this so boxes can be added on as we
    # itterate through the word
    while index1 < len(guess):  # while loop for len less than index1
        if guess[index1] == secret_word[index1]:  # if guess index euqual to secre index
            constant += GREEN_BOX
            # retrun green box and concatenate to constant to print out worlde
        # Don't want this b/c it is going to run the fucntion and return True
        # without doing anything to it contains_char(check_wrd = secret, sngl_char = guess[index1])
        elif contains_char(check_word=secret_word, sngl_char=guess[index1]):
            # calling contains cahr and assigning check_wrd as the same
            # as secret, and char_guess same as guess fo contains char can run on these variables
            # no need for other while statmement b/c we are using contains_char for ywlloe box
            # don't need == True b/c if/esle statemnts are bool statements so we don't need to say eqal to True
            constant += YELLOW_BOX  # adds on yelloe box if contains_char
            # is True
        else:  # can use else b/c its if all else fails do this
            constant += WHITE_BOX  # automatically goes to false and adds
            # white box to constant
        index1 += 1  # put this at end so you don't need to sorry abt putting in
        # between code
        # adds index at athe end and themn goes back up to while loop
    return constant  # will return constant with the emojis!!


if __name__ == "__main__":
    main(secret="codes")
    # 1. makes it so that we can run code as a module
    # 2. possible for other modules to import our functions to resue!!

# end of code!!
