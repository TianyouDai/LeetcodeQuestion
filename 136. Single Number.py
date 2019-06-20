import collections

def singleNumber(nums):
        
    c = collections.Counter(nums)
    for i, j in c.items():
        if j == 1:
            return i
