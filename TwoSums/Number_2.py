from typing import List


def solution(nums: List[int], target: int) -> List[int]:
    charMap = {}

    for i in range(len(nums)):
        temp_result = target - nums[i]

        if temp_result in charMap:
            return [charMap[temp_result], i]
        else:
            charMap[nums[i]] = i

print(solution([3,2,4], 7))