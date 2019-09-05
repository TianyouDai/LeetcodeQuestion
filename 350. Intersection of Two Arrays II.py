class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums = {}
        
        dnums1 = {}
        for x in nums1:
            if x not in dnums1: dnums1[x] = 0
            dnums1[x] += 1
            nums[x] = True
            
        dnums2 = {}
        for x in nums2:
            if x not in dnums2: dnums2[x] = 0
            dnums2[x] += 1
            nums[x] = True
        
        lst = []
        for n in nums:
            if n in dnums1 and n in dnums2:
                lst += [n] * min(dnums1[n], dnums2[n])
        
        return lst

        
