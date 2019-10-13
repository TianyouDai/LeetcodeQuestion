class Solution:
    def checkRecord(self, s: str) -> bool:
        count_a = s.count('A')
        count_l = s.count('L')
        
        if count_a > 1:
            return False
        if count_l>2 and 'LLL' in s:
            return False
        return True
