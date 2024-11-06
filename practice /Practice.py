# print(type(110))
# print(int("20"))
# print(str(20))
# print(int(2.0) + 4 / int("2.0"))
# #print(int(2.0) + 4 / int("2"))
# print("hello")
# print("hello")
# print(bool(1 > 2))
# print("true")
# print(int("87" + "87"))
# print(str(14.0))


def single2(wrd: str) -> list[str]:
    wrd_list: list[str] = []
    for num in range(0, len(wrd)):
        wrd_list.append(wrd[num])
    return wrd_list


def single(impt: str) -> list[str]:
    wrd_list2: list[str] = []
    for char in impt:
        wrd_list2.append(char)
    return wrd_list2


def odd_and_even(l: list[int]) -> list[int]:
    new_list: list[int] = []
    for num in range(0, len(l)):
        if l[num] % 2 == 1:
            if num % 2 == 0:
                new_list.append(l[num])
    return new_list
