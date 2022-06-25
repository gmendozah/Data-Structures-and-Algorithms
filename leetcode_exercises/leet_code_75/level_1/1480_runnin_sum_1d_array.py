from typing import List

def runningSum(self, nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums


print(runningSum(False,[1,2,3,4,5]))
