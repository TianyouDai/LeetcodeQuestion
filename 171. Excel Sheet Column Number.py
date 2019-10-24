class Solution:
    def titleToNumber(self, s: str) -> int:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        d = {}
        for i in range(len(alphabet)):
            d[alphabet[i]]=i+1

        col = 0
        for ch in s:
            col = col * len(alphabet) + d[ch]

        return col
