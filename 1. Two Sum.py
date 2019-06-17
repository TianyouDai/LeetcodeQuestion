def twoSum(nums, target):
    k = 0
    for i in range(0, len(nums)-1):
        k = k + 1
        for j in range(k, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
        
        
