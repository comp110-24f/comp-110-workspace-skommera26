"""Challenge Question 07!"""

__author__ = 730651436

from CQs.cq07.find_max import find_and_remove_max


def test1_find_and_remove_max() -> None:
    """First test use case ensuring function returns expected value"""
    b: list[int] = [4, 49, 60, 14, 60]
    find_and_remove_max(b)
    assert find_and_remove_max(b) == 10


def test2_find_and_remove_max() -> None:
    """Second test use case that mutates input in expected way"""
    b: list[int] = [4, 49, 60, 14, 60]
    find_and_remove_max(b)
    assert b == [4, 49, 14]
    # checks if the mutated list returns right value


def test3_find_and_remove_max() -> None:
    b: list[int] = []
    find_and_remove_max(b)
    assert find_and_remove_max(b) == -1
