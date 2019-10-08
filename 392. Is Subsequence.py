class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for i in s:
            if t.find(i) >= 0:
                tmp = t.find(i)
                t = t[tmp + 1:]
            else:
                return False
        return True
        
                
