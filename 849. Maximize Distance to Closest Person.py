class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        first = 0
        last = len(seats) - 1
        res = 0
        
        while seats[first] == 0:
            first += 1
        
        while seats[last] == 0:
            last -= 1
        
        diff = 0
        pre = first
        
        for i in range(first, last + 1):
            if seats[i] == 1:
                diff = max(diff, i - pre)
                pre = i
     
        res = max(first, diff //2, len(seats) - 1 - last)
        
        return res
