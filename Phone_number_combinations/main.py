from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def backtrack(path: str, next_digits: str) -> None:
            if not next_digits:
                result.append(path)
            else:
                for c in phone[int(next_digits[0])]:
                    backtrack(path + c, next_digits[1:])


        result = []
        backtrack("", digits)
        return result


