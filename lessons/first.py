def get_first(input: list[int]) -> int:
    """Return the first element (index 0) of the input list"""
    if len(input) == 0:
        return -1
    return input[0]


def remove_first(input: list[int]) -> None:
    """Remove the first element (index 0) of the input list"""
    if len(input) > 0:
        input.pop(0)
        # if length is 0 will not do anything so we want if greater than 0, then it will remove


def remove_and_get_first(input: list[int]) -> int:
    """Remove AND return the first element (index 0) of the input list"""
    first: int = input[0]
    input.pop(0)
    return first
    # if it was without first, it would give error when run, because it wwon't return 4 like we wanted in the first_test file!
