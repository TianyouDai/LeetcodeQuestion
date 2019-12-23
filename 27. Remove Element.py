class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = 0
        for i in nums:
            if  i != val:
                nums[length] = i
                length += 1
        return length
        
        
