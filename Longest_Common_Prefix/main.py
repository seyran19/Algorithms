from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    strs.sort()
    answer = ""

    for i in range(len(min(strs, key=lambda x: len(x)))):
        if strs[0][i] == strs[-1][i]:
            answer += strs[0][i]
        else:
            return answer


print(longestCommonPrefix(["flower", "flow", "flight"]))
