class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        res = 1
        a = nums[-1] * nums[-2] * nums[-3]
        b = nums[-1] * nums[0] * nums[1]
  
        return max(a, b)
        
        
