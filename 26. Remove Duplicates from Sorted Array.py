class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == None:
            return 0
        
        if len(nums) == 1:
            return 1

        curElem = 0
        nextElem = 1
        while nextElem < len(nums):
            if nums[nextElem] > nums[curElem]:
                curElem += 1
                nums[curElem] = nums[nextElem]
            nextElem += 1
        return curElem + 1
        
