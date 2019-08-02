class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        result = []
        remainder = 0
        for bit in A:
            remainder = (2*remainder + bit) % 5
            result.append(remainder == 0)
        return result
