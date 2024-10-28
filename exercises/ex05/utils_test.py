"""EX05"""

__author__ = "730641436"

# start of the code!

from exercises.ex05.utils import only_evens, sub, add_at_index


# Testings on only_evens functions (one edge case and two use cases)
def test_edge_only_evens() -> None:
    """Testing edge case on only_evens function"""
    assert only_evens([]) == []


# testung to make sure that the when given a empty bracket it will return empty bracket
# is a edge case b/c we are testing out of the ordinary variables


def test_first_use_only_evens() -> None:
    # return value will be None for all sicne we are not returning anything!
    """Testing first use case shwoing no mutation on only_evens input function"""
    test_list: list[int] = [1, 4, 6, 8]  # list to be used
    only_evens(test_list)
    # calling the function and asking to run it
    assert (test_list) == test_list
    # once run, making sure the function did not modify the original list and kept it the same


def test_second_use_only_evens() -> None:
    # return value will be None for all sicne we are not returning anything!
    """Testing second use case making sure it returns right items"""
    test_list1: list[int] = [3, 6, 8, 2, 9, 14, 6]  # list to use
    only_evens(test_list1)  # runs the function with that list
    assert only_evens(test_list1) == [6, 8, 2, 14, 6]
    # making sure that the function returns the right output needed


# Testing on sub function (one edge case and two use cases)


def test_sub_edge() -> None:
    # return value will be None for all sicne we are not returning anything!
    """Testing to make sure that when given non-ordinary inputs it give sout the correct output"""
    test_list2: list[int] = [1, 5, 8, 9]  # test list
    sub(test_list2, 5, 4)  # rcalling og function to run with the list
    assert sub(test_list2, 5, 4) == []
    # making sure that when the function is called with the lsit, and is giving an index out of bounds (index 1 is greater than len of list) it will return empty brackets


def test_sub_use1() -> None:
    # return value will be None for all sicne we are not returning anything!
    """Testing functions returns the og list not mutated"""
    test_list3: list[int] = [1, 6, 8, 3, 6, 2]  # test lsit
    sub(test_list3, 1, 5)  # calling function w that list
    assert test_list3 == test_list3
    # making sure that og list was not mutated by the function when called
    # edge case b/cwe are making sure it is running with inputs that would normally be given


def test_sub_use2() -> None:
    # return value will be None for all sicne we are not returning anything!
    """Testing functions resturns input that we want"""
    test_list4: list[int] = [1, 7, 9, 13, 56, 7, 9]  # test list
    assert sub(test_list4, 2, 6) == [9, 13, 56, 7]
    # making sure that when the function is caleld with the list it returns the list that we want


# Testing add_at_index function using use and edge case tests

import pytest


def test_add_at_index_raises_indexerror():
    # uses pytest here to make sure erorr is raised properly
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    test_list5: list[int] = []  # test list
    with pytest.raises(IndexError):  # code to ensure a error is raised
        add_at_index(test_list5, 2, 4)
        # an IndexError is raised for the case when given a empty list, but given a out of bounds index


def test_add_at_index_raises_indexerror2():
    """Test the add_at_index insers 2 at index 0"""
    test_list10: list[int] = []  # test list
    add_at_index(
        test_list10, 2, 0
    )  # calling the function; this one does modify the list
    assert test_list10 == [
        2
    ]  # making sure that list if modified the way we want it to be modified
    # since the og function returns None, we do not havr to call function when saying assert


def test_add_at_index_use_test() -> None:
    # return value will be None for all sicne we are not returning anything!
    """Test that add_at_index function gives the right return list"""
    test_list6: list[int] = [2, 4, 6, 8]  # test list
    add_at_index(test_list6, 10, 2)  # calls the function w/ test list
    assert test_list6 == [2, 4, 10, 6, 8]
    # asserting that the test list if modified the way is should be here and returning the right list


def test_add_at_index_use_test2() -> None:
    # return value will be None for all sicne we are not returning anything!
    """Test that add_at_index function mutates the original list"""
    test_list7: list[int] = [3, 9, 6, 10, 14]  # test list
    add_at_index(test_list7, 5, 4)  # calling function
    assert test_list7 != add_at_index(test_list7, 5, 4)
    # making sure that the test list is not equal to the None value that would come out when called
