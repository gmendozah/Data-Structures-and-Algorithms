def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    n = len(input_list)
    # 1. find out the pivot
    pivot = findPivot(input_list, 0, n - 1)
    # If we didn't find a pivot,
    # then array is not rotated at all
    if pivot == -1:
        return binarySearch(input_list, 0, n - 1, number)

    # search in two subarrays around pivot
    if input_list[pivot] == number:
        return pivot
    if input_list[0] <= number:
        return binarySearch(input_list, 0, pivot - 1, number)
    return binarySearch(input_list, pivot + 1, n - 1, number)


def binarySearch(arr, low, high, key):
    if high < low:
        return -1

    # low + (high - low)/2;
    mid = int((low + high) / 2)

    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binarySearch(arr, (mid + 1), high, key)
    return binarySearch(arr, low, (mid - 1), key)


def findPivot(arr, low, high):
    # base cases
    if high < low:
        return -1
    if high == low:
        return low

        # low + (high - low)/2;
    mid = int((low + high) / 2)

    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return mid - 1
    if arr[low] >= arr[mid]:
        return findPivot(arr, low, mid - 1)
    return findPivot(arr, mid + 1, high)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])  # Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])  # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])  # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])  # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])  # Pass
test_function([[1, 2, 3], 10])  # Pass
test_function([[], 100])  # Pass
