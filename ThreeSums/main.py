def threeSumCloset(nums, target):
    if not nums: return []
    result_list = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]: continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            temp_result = nums[left] + nums[right] + nums[i]
            result_list.append(temp_result)

            if temp_result > target: right -= 1
            elif temp_result <= target: left += 1

            while left < right and nums[left] == nums[left - 1]: left += 1

    return min(result_list, key=lambda x: abs(target - x))


print(threeSumCloset([0, 0, 0], 0))