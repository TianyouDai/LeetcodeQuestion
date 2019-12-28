class Solution:    
    def getLength(a, number):
        Length = 0
        while number != 0:
            Length += 1
            number = number // 10    
        return Length
    
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if self.getLength(nums[i]) %2 == 0:
                count += 1
            
        return count
    
            
