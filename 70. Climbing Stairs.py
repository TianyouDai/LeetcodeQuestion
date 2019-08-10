class Solution:
    def climbStairs(self, n: int) -> int:
        step = [1,1]
        for i in range(2,n+1):
            step.append(step[i-1] + step[i-2])
        return step[n]
        
