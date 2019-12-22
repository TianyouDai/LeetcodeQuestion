class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1] < target:
            return len(nums)
        
        for i, n in enumerate(nums):
            if target == n:
                return i
            elif n > target:
                j = i
                while j:
                    if target > nums[j-1]:
                        return j
                    j -= 1
                else:
                    return 0
