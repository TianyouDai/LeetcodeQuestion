class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = int(a, 2)
        num2 = int(b, 2)
        res = num1 + num2
        res = bin(res)[2:]
        return str(res)
        
