def reverse(x):
    if x < 0:
        return -reverse(-x)
    result = 0
    while x:
        result = result * 10 + x % 10
        x //= 10
    return result if result <= 0x7fffffff else 0
