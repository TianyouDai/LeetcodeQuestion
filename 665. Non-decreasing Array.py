class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        change_count = 0

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if change_count:
                    return False
                if i == 1 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
                change_count = 1
        return True
        
        
