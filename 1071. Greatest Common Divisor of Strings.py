class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1) 
        len2 = len(str2) 
        gcd = 1

        if len1 == len2:
            if str1 == str2:
                return str1
            else: return ""
        elif len1 > len2:
            smaller_len = len2
            larger_len = len1
        else:
            smaller_len = len1
            larger_len = len2
        
        for i in range(1, smaller_len + 1):
            if len1 % i == 0 and len2 % i == 0:
                gcd = i
        
        div1 = len1 // gcd
        div2 = len2 // gcd
    

        if not (div1 * str1[:gcd] == str1) and (div2 * str2[:gcd] == str2):
            return ""
        else:      
            return str1[:gcd]
    
    
    
    
    
