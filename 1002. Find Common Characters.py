from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:    
        c = Counter(A[0])
        
        for i in range(1,len(A)):
     
            c = c & Counter(A[i]) 
            
        return c.elements()
