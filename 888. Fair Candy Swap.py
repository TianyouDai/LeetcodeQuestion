class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_a = sum(A)
        sum_b = sum(B)
        diff = (sum_a - sum_b) // 2
        adict = {x: True for x in A}
        for b in B:
            if (b + diff) in adict:
                return [b + diff, b]
                    
                    
                
