from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        nums.sort()
        result = []

        for index, value in enumerate(nums):
            if index > 0 and nums[index - 1] == value: continue

            left = index + 1
            right = len(nums) - 1

            while left < right:
                temp_result = value + nums[left] + nums[right]

                if temp_result > 0:
                    right -= 1
                elif temp_result < 0:
                    left += 1
                else:
                    result.append([value, nums[right], nums[left]])
                    left += 1
                while left < right and nums[left] - 1 == nums[left]: continue

        return result