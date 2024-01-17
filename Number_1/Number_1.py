from collections import defaultdict


def solution(nums, target):
    two_sum = defaultdict(list)
    result = set()

    for a in range(len(nums) - 1):
        for b in range(a + 1, len(nums)):
            two_sum[nums[a] + nums[b]].append((a, b))

    for temp_check in two_sum:
        temp_result = target - temp_check

        if not temp_result in two_sum: continue

        for a, b in two_sum[temp_check]:
            for c, d in two_sum[temp_result]:
                if a != c and a != d and b != c and b != d:
                    result.add(tuple(sorted([nums[a], nums[b], nums[c], nums[d]])))

    return result


print(solution([2, 2, 2, 2, 2], 8))

