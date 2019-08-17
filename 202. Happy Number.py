class Solution:
    def isHappy(self, n: int) -> bool:
        def is_happy(n):
            res = (n == 1) + (n == 7) + (n < 10)
            if res == 2:
                return True
            if res == 0:
                return is_happy(sum(int(x)**2 for x in str(n)))
            else:
                return False
        return is_happy(n)
