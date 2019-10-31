class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        res = []
        index = 0
        char = S[0]

        for i, s in enumerate(S):
            if s != char:
                if i - index >= 3:
                    res.append([index, i - 1])

                index = i
                char = s

        if i - index >= 2:
            res.append([index, i])


        return res
