class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        for i in range(m):
            res.append(nums1[i])
    
        for j in range(len(nums2)):
            res.append(nums2[j])
        res = sorted(res)
        
        for k in range(len(nums1)):
            nums1[k] = res[k]
        
