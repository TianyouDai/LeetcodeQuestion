class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        
        if len(cost) == 2:
            return min(cost[0], cost[1])
        
        f1 = cost[0]
        f2 = cost[1]
        
        for i in range(2, len(cost)):
            current = cost[i] + min(f1, f2)
            f1, f2 = f2, current
        
        return min(f1,f2)
            
            
            
        
