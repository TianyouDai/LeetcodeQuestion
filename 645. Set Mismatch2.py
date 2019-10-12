class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        fz = [0 for _ in range(len(nums)+ 1)]
        fz[0] = -1
        
        for x in nums:
            fz[x] += 1
        
        ans = [0, 0]
        for i, x in enumerate(fz):
            if x == 2: ans[0] = i
            if x == 0: ans[1] = i
        
        return ans
