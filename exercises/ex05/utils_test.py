"""EX05"""

__author__ = "730641436"

# start of the code!

from exercises.ex05.utils import only_evens, sub, add_at_index


# Testings on only_evens functions (one edge case and two use cases)
def test_edge_only_evens() -> None:
    """Testing edge case on only_evens function"""
    assert only_evens([]) == []


def test_first_use_only_evens() -> None:
    """Testing first use case shwoing no mutation on only_evens input function"""
    test_list: list[int] = [1, 4, 6, 8]
    only_evens(test_list)
    assert (test_list) == test_list


def test_second_use_only_evens() -> None:
    """Testing second use case making sure it returns right items"""
    test_list1: list[int] = [3, 6, 8, 2, 9, 14, 6]
    only_evens(test_list1)
    assert only_evens(test_list1) == [6, 8, 2, 14, 6]


# Testing on sub function (one edge case and two use cases)


def test_sub_edge() -> None:
    """Testing to make sure that when given non-ordinary inputs it give sout the correct output"""
    test_list2: list[int] = [1, 5, 8, 9]
    sub(test_list2, 5, 4)
    assert sub(test_list2, 5, 4) == []


def test_sub_use1() -> None:
    """Testing functions returns the og list not mutated"""
    test_list3: list[int] = [1, 6, 8, 3, 6, 2]
    sub(test_list3, 1, 5)
    assert test_list3 == test_list3


def test_sub_use2() -> None:
    """Testing functions resturns input that we want"""
    test_list4: list[int] = [1, 7, 9, 13, 56, 7, 9]
    assert sub(test_list4, 2, 6) == [9, 13, 56, 7]


# Testing add_at_index function using use and edge case tests

import pytest


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    test_list5: list[int] = []
    with pytest.raises(IndexError):
        add_at_index(test_list5, 2, 4)
        # an IndexError is raised for the case when the add_at_index is given an <index_to_insert_num>
        # that is greater than the length of our <list_object>


def test_add_at_index_use_test() -> None:
    """Test that add_at_index function gives the right return list"""
    test_list6: list[int] = [2, 4, 6, 8]
    add_at_index(test_list6, 10, 2)
    assert test_list6 == [2, 4, 10, 6, 8]


def test_add_at_index_use_test2() -> None:
    """Test that add_at_index function mutates the original list"""
    test_list7: list[int] = [3, 9, 6, 10, 14]
    add_at_index(test_list7, 5, 4)
    assert test_list7 != add_at_index(test_list7, 5, 4)
