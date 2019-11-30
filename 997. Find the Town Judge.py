class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusted = [0 for _ in range(N + 1)]        
        trusts = [0 for _ in range(N + 1)]
        
        for i in trust:
            trusted[i[1]] += 1
            trusts[i[0]] += 1
        
        for j in range(1, len(trusts)):
            if trusts[j] == 0 and trusted[j] == N - 1:
                return j
        return -1
            
      
