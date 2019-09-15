class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        inner = []
        res = []
        for i in range(0, len(A)):
            #flipping the image
            inner = A[i][::-1]
            #inverting the image
            for j in range(0, len(inner)):
                if inner[j] == 0:
                    inner[j] = 1
                else:
                    inner[j] = 0
            res.append(inner)
            inner = []
        return res 
