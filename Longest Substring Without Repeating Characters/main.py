def Longest_string(map: str) -> int:
    char_map = {}
    left = 0
    result = 0

    for right in range(len(map)):
        if map[right] not in char_map or char_map[map[right]] < left:
            char_map[map[right]] = right
            result = max(result, right - left + 1)
        else:
            left = char_map[map[right]] + 1
            char_map[map[right]] = right

    return result


print(Longest_string("abcabcbb"))