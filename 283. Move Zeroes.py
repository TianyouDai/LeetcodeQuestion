def moveZeroes(nums):
    zeros = nums.count(0)
    if zeros > 0:
        ind = 0
        while zeros >= 0:
            nums.pop(nums.index(0))
            nums.append(0)
            zeros -= 1
    return nums
