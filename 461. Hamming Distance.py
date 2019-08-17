class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        strX = format(x, 'b').zfill(31)
        strY = format(y, 'b').zfill(31)
        c = 0
        
        for i in range(len(strX)):
            if strX[i] != strY[i]:
                c += 1
        
        return c
        
