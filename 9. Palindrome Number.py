class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        
        
        i = list(str(x))
        j = list(str(x)[::-1])
        
        for i,j in zip(i, j):
            if i != j:
                return False 
        return True 
        
