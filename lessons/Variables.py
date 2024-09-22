"""Variables + conditionals!!"""


def less_than_10(num: int) -> None:
    # tell me if num less than 10
    age: int = 10
    age = age - 1
    print(age)
    if num < 10:
        print("small number")
    else:
        print("big number")


print("have a nice day!")
less_than_10(num=5)
# if num=11, when return type is bool and there is no else statement, would give None b/c no code to say what to do if fasle"""
# for return, DO NOT put colon"""


def get_weather_report() -> str:
    weather: str = input("what is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")

    return weather


get_weather_report()

age: int = 10
age = age + 1
