def isUgly(num):
    if num == 0:
        return False

    if num == 1:
        return True

    elif num % 2 == 0:
        return isUgly(num/2)

    elif num % 3 == 0:
        return isUgly(num/3)
        
    elif num % 5 == 0:
        return isUgly(num/5)

    return False
