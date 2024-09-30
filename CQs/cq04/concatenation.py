"""Challenge Question 03!"""

__author__ = 730651436

if (
    __name__ == "__main__"
):  # makes it so that the function call still occurs but will not be printed when imported but will be printed when called in reppul

    def concat(str1: str, str2: str) -> str:  # function signature
        return str1 + str2  # return type

    word1: str = "happy"  # global variables
    word2: str = "tuesday"  # global variables

    print(concat(word1, word2))  # need print in front so it prints the values
