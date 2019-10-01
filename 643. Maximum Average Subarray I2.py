class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) <= k:
            return sum(nums) / k
       
        res_sum = sum(nums[:k])
        avg = res_sum / k
             
        for i in range(k, len(nums)):
            res_sum = res_sum + nums[i] - nums[i - k]
            res = res_sum / k
            if res > avg: 
                avg = res
        return avg
        
