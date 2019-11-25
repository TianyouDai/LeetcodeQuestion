class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        eNums = list(enumerate(nums))        
        eNums = sorted(eNums, key=lambda x: x[1])
        
        diff = []        
        for i, iv in enumerate(nums):
            _, jv = eNums[i][0], eNums[i][1]
            
            if iv != jv:
                diff.append(i)
                
        small, big = len(nums), 0        
        for d in diff:            
            small = min(small, d) 
            big   = max(big, d)
        
        if small == len(nums) and big == 0:
            return 0
        
        return big - small + 1
