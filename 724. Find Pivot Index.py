class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return -1
        total = sum(nums)
        answer_so_far = 0
        for i in range(0, len(nums)):
            if (total - nums[i]) / 2 == answer_so_far:
                return i
            answer_so_far += nums[i]
        return -1
                
        
