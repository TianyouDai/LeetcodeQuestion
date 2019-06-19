def findErrorNums(nums):
    if nums == []:
        return [0,0]
    nums.sort()
    dup = 0
    loss = 0
    s = nums[0]
    n = len(nums)
    for i in range(1,n):
        s += nums[i]
        if nums[i] == nums[i-1]:
            dup = nums[i]
            s -= nums[i]
    S = (1+n)*n/2
    loss = int(S - s)
    return [dup,loss]
