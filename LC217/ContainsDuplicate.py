from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ans = set()
        # x will represent the index in the list nums
        for x in range(len(nums)):
            if nums[x] in ans:
                return True
            ans.add(nums[x])
        return False

# Example usage
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 1]  # Example list of numbers
    solution = Solution()
    result = solution.containsDuplicate(nums)
    print("Contains duplicates:", result)
