from typing import List


def maxArea(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    result = 0

    while left < right:
        if height[right] < height[left]:
            temp_result = height[right] * (right - left)
            if temp_result > result: result = temp_result
            right -= 1
        else:
            temp_result = height[left] * (right - left)
            if temp_result > result: result = temp_result
            left += 1
    return result

