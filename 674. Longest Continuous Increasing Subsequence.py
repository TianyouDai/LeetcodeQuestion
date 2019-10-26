class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        length = len(nums)
        a = 0
        b = 0
        if length == 0: 
            return 0
        
        for i in range(length - 1):
            b = b + 1
            if nums[i + 1] <= nums[i]:
                if b > a: a = b
                b = 0
            
        return max(a, b + 1)
        
