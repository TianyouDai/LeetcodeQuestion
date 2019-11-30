class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count = 0
        for i in nums:
            if i != target:
                count += 1
            elif i == target:
                return count
    
        if count == len(nums):
            return -1
