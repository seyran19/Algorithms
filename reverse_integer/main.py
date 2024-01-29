def reverse(x: int) -> int:
    if x > 0:
        return int(str(x)[::-1])
    elif x < 0:
        result = str(x)[::-1]
        return - int(result[0: len(result) - 1])
    else:
        return 0




print(reverse(-1202))
