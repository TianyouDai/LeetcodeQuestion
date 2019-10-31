class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        res = []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        len_odd = len(odd)
        len_even = len(even)

        if (len_even >= len_odd):
            for i in range(len_even):
                res.append(even[i])
                res.append(odd[i])
        else:
            for i in range(len_even):
                res.append(odd[i])
                res.append(even[i])

        return res
