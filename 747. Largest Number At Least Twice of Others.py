class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n = sorted(nums)
        if len(nums) == 1:
            return 0

        if n[-1] >= n[-2] * 2:
            return nums.index(n[-1])
        else:
            return -1
