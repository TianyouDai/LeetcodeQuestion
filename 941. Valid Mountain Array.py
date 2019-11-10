class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        i = 0
        j = len(A) -1
        
        while i + 1 < len(A) and A[i] < A[i+1]:
            i += 1
        
        while j - 1 > 0 and A[j] < A[j-1]:
            j -= 1
        
        if j == i and (i != 0) and j != len(A) - 1:
            return True
        return False
            
        
