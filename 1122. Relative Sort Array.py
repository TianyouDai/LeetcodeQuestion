class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        temp = []
        for i in arr2:
            for j in arr1:
                if i == j:
                    res.append(j)

        for t in arr1:
            if t not in res:
                temp.append(t)

        temp = sorted(temp)

        for w in temp:
            res.append(w)
        return res
