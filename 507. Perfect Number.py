def checkPerfectNumber(num):
    if num <= 1:
        return False
    res = 1
    i = 2
    while i * i < num:
        if num % i == 0:
            res += i + num / i
        i += 1   
            
    if res == num:
        return True
    return False


        
