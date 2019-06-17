def convertToBase7(num):
    positive = (num >= 0)
    if not positive: num = -num

    def find_seven(num):
        if num == 0:
            return 0
        else:
            return num % 7 + 10 * find_seven(num//7)

    return str(find_seven(num)) if positive else str(-find_seven(num))
