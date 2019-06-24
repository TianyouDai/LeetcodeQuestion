def addDigits(num):
    res = 0
    d = len(str(abs(num)))

    if d == 1:
        return num
    else:
        res = addDigits(num % 10 + addDigits(num // 10))

    return res
