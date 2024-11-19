def factorial(n: int) -> int:
    """Compute the factorial of n."""
    # Base case: n is 0 or 1
    # recusrive case: n * recursive call with n - 1 as argument
    if n == 1 or n == 0:
        return 1
    # base case --> says to stop here and like not loop through infinitly
    else:
        return n * factorial(n - 1)
    # will recurse through where it will times n by n-1 until reaches base case where it will return one and then will take that one times by the preivous n value of the frame above
