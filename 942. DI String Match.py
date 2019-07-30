class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        if not S:
            return []
        res = []

        l,r = 0, len(S)
        for i in S:
            if i == "I":
                res.append(l)
                l += 1
            else:
                res.append(r)
                r -= 1
        res.append(r)
        return res
