class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        res = []
        i = 0
        
        while len(res) < n:
            if n % 2 == 0:
                if i == 0:
                    pass
                else:
                    res.append(i)
                    res.append(-i)
                i += 1
            
            else:
                if i == 0:
                    res.append(i)
                else:
                    res.append(i)
                    res.append(-i)
                i += 1
            
        return res
