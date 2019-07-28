class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = 0
        for i in digits:
            a = a * 10 + i
        tmp = a + 1
        
        res = list()
        while tmp:
            res.insert(0, tmp % 10)
            tmp //= 10
        return res

    
        
