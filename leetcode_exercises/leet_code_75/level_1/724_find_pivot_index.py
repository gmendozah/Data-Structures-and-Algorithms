from typing import List

def pivotIndex(self, nums: List[int]) -> int:
    S = sum(nums)
    left_sum = 0
    for i, x in enumerate(nums):
        if left_sum == (S - x - left_sum):
            return i
        left_sum += x
    return -1

print(pivotIndex(False, [2,1,-1]))