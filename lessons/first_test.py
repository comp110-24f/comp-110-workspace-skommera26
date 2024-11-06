# need to import!
from lessons.first import get_first, remove_and_get_first, remove_first

# no need to add another from statement, can just add onto the original import statement to add another function


def test_name() -> None:  # no need to worrry abt parameters or return types
    """Testing get_first function returns the first element in a typical input"""
    # can have line of coe that gives list here as well
    assert get_first([4, 5, 6, 7]) == 4
    # just need assert statement here
    # passed unti test yay!


def test_get_first_edge_case() -> None:
    """Testing get first on empy list"""
    # edge case = empty list or something that is unusual
    assert get_first([]) == -1


def test_remove_first_use_case() -> None:
    """Testinf remove_first returns nothing"""
    a: list[int] = [4, 5, 6, 7]
    remove_first(a)
    assert a == [5, 6, 7]
    # bool uses ==


# now for new impoted function, need to create a new function definition
def test_remove_and_get_first() -> None:
    """Testing remove_and_get_first returns the first element in a use case"""
    a: list[int] = [102, 45, 76]
    remove_and_get_first(a)
    assert a == [45, 76]
    # dic string stell us what our unit test is really telling us


def test_remove_first_edge_case() -> None:
    """Testing remove first on empty list should not do anything"""
    a: list[int] = []
    remove_first(a)  # calling function so put parenthases
    assert a == []
