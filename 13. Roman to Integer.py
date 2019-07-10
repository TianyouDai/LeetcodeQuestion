class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        prev = ''
        for i in s:
            res = res + dict[i]
            if prev == 'I' and i in {'V', 'X'}:
                res = res - 2
            elif prev == 'X' and i in {'L', 'C'}:
                res = res - 20
            elif prev == 'C' and i in {'D', 'M'}:
                res = res - 200
            prev = i
        
        return res
        
