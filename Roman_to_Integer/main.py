def romanToInt(s: str) -> int:
    ROMAN_TO_INTEGER = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    last = curr = result = 0

    for c in s[::-1]:
        last, curr = curr, ROMAN_TO_INTEGER[c]
        result += curr if curr >= last else - curr

    return result

print(romanToInt("VI"))