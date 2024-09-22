"""practice w/ conditionls"""


def less_than_10(num: int) -> None:
    """tell me if num less than 10"""
    if num < 10:
        print("small number")
    else:
        print("big number")


(less_than_10(num=1))
"""if num=11, when return type is bool and there is no else statement, would give None b/c no code to say what to do if fasle"""
"""for return, DO NOT put colon"""


def should_i_eat(hungry: bool) -> None:
    "tells me wheater or not to east base don hunger"
    if hungry:  # conditional/ bool expression
        """could have if hungry is True or just hingry"""
        print("Eat some food!")  # then block
    else:
        print("do your hw!")
    print("I'm proud of you :)")  # either way be kind!


should_i_eat(hungry=False)


def check_first_letter(
    word: str, letter: str
) -> str:  # ALWAYS put a colon after the return type!!!
    print("hello")
    """chekcs if firtst lettter of word is letter"""
    if letter == word[0]:  # put a colon after this as well
        return "match!"
    else:  # colon for this too
        return "no match!"


# for return types None, you can take out return and put in print instead

print(check_first_letter(word="happy", letter="s"))
