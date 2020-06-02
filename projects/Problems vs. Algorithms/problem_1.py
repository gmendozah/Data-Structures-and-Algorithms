def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None:
        return None
    else:
        try:
            test_val = int(number)
        except ValueError:
            print("That's not an int!")
            return None

    if number < 0:
        print('Cannot calculate square root of negative numbers')
        return None

    return _sqrt(0, number, number)


def _sqrt(low, high, N):
    # If the range is still valid
    if low <= high:
        # Find the mid-value of the range
        mid = (low + high) // 2
        # Base Case
        if (mid * mid <= N) and ((mid + 1) * (mid + 1) > N):
            return mid
            # Condition to check if the
        # left search space is useless
        elif mid * mid < N:
            return _sqrt(mid + 1, high, N)
        else:
            return _sqrt(low, mid - 1, N)
    return low


# edge cases
print("Pass" if (None == sqrt(-9)) else "Fail")  # Pass
print("Pass" if (None == sqrt(None)) else "Fail")  # Pass
print("Pass" if (None == sqrt("Hello")) else "Fail")  # Pass
# normal cases
print("Pass" if (3 == sqrt(9)) else "Fail")  # Pass
print("Pass" if (0 == sqrt(0)) else "Fail")  # Pass
print("Pass" if (4 == sqrt(16)) else "Fail")  # Pass
print("Pass" if (1 == sqrt(1)) else "Fail")  # Pass
print("Pass" if (5 == sqrt(27)) else "Fail")  # Pass
print("Pass" if (6 == sqrt(27)) else "Fail")  # Fail
print("Pass" if (7 == sqrt(27)) else "Fail")  # Fail
