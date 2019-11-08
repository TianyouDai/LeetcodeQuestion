class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0 
        c = collections.Counter(time)
        keys = list(c.keys())
		
        for i in range(len(list(c.keys()))):
            if keys[i] % 60 == 0 or  keys[i] % 60 == 30:
                res +=  (c[keys[i]])*(c[keys[i]]-1)//2
                
            for j in range(i+1, len(keys)):
                if (keys[i] + keys[j]) % 60 == 0 :
                    res += c[keys[i]] * c[keys[j]]

        return res 
             
               
   
                
        
