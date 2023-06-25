from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = 0
        for index , num in enumerate(nums):
            if num != val:
                nums[curr] = nums[index]
                curr += 1
        return curr

        # keep track of a pointer where we place values not equal to val
        # aka amount of values not equal to val
        # let's loop through the array
        # let's check each element and check if it is equal to val
        # if not equal to val, we set num[curr] = current val
        # increase curr by 1
