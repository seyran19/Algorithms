def intToRoman(self, num: int) -> str:
    ROMAN = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    INTEGER = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    result = ""

    for i, symb in zip(INTEGER, ROMAN):
        count = num // i
        num -= count * i
        result += symb * count
    return result
