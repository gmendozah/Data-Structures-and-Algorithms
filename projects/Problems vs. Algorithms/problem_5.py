import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        print('Cannot get min and max from empty array')
        return None

    min_num, max_num = 0, 0
    if len(ints) > 1:
        min_num = ints[0]
        max_num = ints[1]
    else:
        min_num = ints[0]
        max_num = ints[0]

    for number in ints:
        if number < min_num:
            min_num = number
        if number > max_num:
            max_num = number

    return min_num, max_num


# Example Test Case of Ten Integers
num_list = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(num_list)

print("Pass" if ((0, 9) == get_min_max(num_list)) else "Fail")  # Pass

print("Pass" if ((0, 9) == get_min_max([0, 9])) else "Fail")  # Pass
print("Pass" if ((1, 2) == get_min_max([1, 2])) else "Fail")  # Pass
print("Pass" if ((0, 0) == get_min_max([0])) else "Fail")  # Pass
