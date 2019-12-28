class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)
        nums = sorted(nums)
        return nums[l//2]
        
