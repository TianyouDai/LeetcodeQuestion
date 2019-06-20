def arrayPairSum(nums):
    nums.sort()
    i = 0
    res = 0
    while i < len(nums):
        res = res + min(nums[i], nums[i + 1])
        i = i + 2
    return res
