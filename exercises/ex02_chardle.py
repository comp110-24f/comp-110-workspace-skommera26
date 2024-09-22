"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730641436"

# start of the code!


# function signature!
def input_word() -> (
    str
):  # if return type is string you need a return value at the end of function!
    word: str = input("Enter a 5-character word: ")  # local variable!!!
    if len(word) == 5:  # this will check if the word entered is equal to length 5
        return word  # if so will return the word so it can be stored and sued later
    elif (
        len(word) > 5 or len(word) < 5
    ):  # this is to show if len(word) is greater than or less than 5
        print(
            "Error: Word must contain 5 characters."
        )  # put print here because if it was return it would skip the return statement in next line and use that return statement of the error message
        quit()  # I put this here because we want the function to stop running once the word is more thant 5 character
        # putting it here ensures that error statement is printed ans it stops function without disturbing other aspects of function
    return word  # this ensure staht the returan value overall will be word and not the error message


def input_letter() -> str:
    letter: str = input("Enter a single character: ")  # local variable!!!
    if len(letter) == 1:  # will return the schar since it is exaclty 1 character
        return letter  # this will ensure that the return value is stored as the schar (single character)
    elif (
        len(letter) > 1 or len(letter) < 1
    ):  # checks if schar is more than 1 or less than 1
        print(
            "Error: Character must be a single character."
        )  # if so it will print this eror message;
        # there is print because if there was a return statement then it would take that into memepry and ignore the return statement below
        quit()  # this ensures that the functions is "quitted" that will not run if the elif statement is true
    return letter  # ensures that the return statement will always be stored as the signle character


def contains_char(check_word: str, check_letter: str) -> None:
    # this will return no value, so all the code will be print statements not return statements
    print(
        "Searching for", check_letter, "in", check_word
    )  # this is a print functions that will tell the reader whatt he function is doing, in this case it is searching for the letter in the word given
    char_count: int = (
        0  # char_count will be used to keep track of how mnay times a character is found, or how many times it is seen
    )
    # since we can't use a while function we have to induvidually check each letter's index to see if it matches the letter, hence the many if statements

    if check_word[0] == check_letter:
        print(check_letter, "found at index 0")
        char_count += 1  # check if at index 0 is equal to letter; if so will print the fucntion and add char_count
    if check_word[1] == check_letter:
        print(check_letter, "found at index 1")
        char_count += 1  # check if at index 1 is equal to letter; if so will print the fucntion and add char_count; if not will continue to next function
    if check_word[2] == check_letter:
        print(check_letter, "found at index 2")
        char_count += 1  # check if at index 2 is equal to letter; if so will print the fucntion and add char_count; if not will continue to next function
    if check_word[3] == check_letter:
        print(check_letter, "found at index 3")
        char_count += 1  # check if at index 3 is equal to letter; if so will print the fucntion and add char_count; if not will continue to next function
    if check_word[4] == check_letter:
        print(check_letter, "found at index 4")
        char_count += 1  # check if at index 4 is equal to letter; if so will print the fucntion and add char_count; if not will continue to next function
    # not need for index five since the index of a 5 letter funcition will only go up until 4, and the length will stay at 5

    if (
        char_count == 1
    ):  # after loop is completed it goes to next code at same level as the while code, and executes this line of code by seing if the if statement is true
        print(
            char_count, "instance of", check_letter, "found in", check_word
        )  # if true it prints out this print statment
    if char_count > 1:
        print(char_count, "instances of", check_letter, "found in", check_word)
    elif char_count == 0:  # if not then goes to elif and prints this out
        print("No instances of", check_letter, "found in", check_word)


def main() -> (
    None
):  # this is the main function that bascially ties all the functions togther so they can perform togther
    contains_char(
        check_word=input_word(), check_letter=input_letter()
    )  # we are setting the check_word equal to input word so that when main is called it goes to input_word first, completes, that and does the same to input_letter then goes to contains_char to complete that part


if __name__ == "__main__":
    main()
