def myAtoi(s: str) -> int:
    s = s.strip()
    answer = ""

    for symbol in s:
        if symbol.isdigit() or symbol == "-":
            answer += symbol
    return int(answer)