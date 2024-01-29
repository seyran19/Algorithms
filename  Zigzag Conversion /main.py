def convert(s: str, numRows: int) -> str:
    if numRows == 1: return s

    current = 0
    rows = [""] * numRows
    is_going_down = False

    for symbol in s:
        rows[current] += symbol

        if current == 0 or current == numRows - 1:
            is_going_down = not is_going_down

        current += 1 if is_going_down else -1

    return ''.join(rows)
