class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = k = nums[0]    
        for i in nums[1:]:
            if k < 0: k = 0
            k += i
            res = res if res > k else k 
        return res
            
            
        
