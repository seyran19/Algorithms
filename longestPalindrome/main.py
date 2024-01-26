def longestPalindrome(s: str) -> str:
    result = ""

    def is_poly(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

    for i in range(len(s)):
        op_1 = is_poly(i, i)
        op_2 = is_poly(i, i + 1)

        if len(op_1) > len(result):
            result = op_1
        if len(op_2) > len(result):
            result = op_2

    return result