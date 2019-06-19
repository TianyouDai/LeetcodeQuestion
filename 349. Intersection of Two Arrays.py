def intersection(nums1, nums2):
    r = []
        
    nums1.sort()
    nums2.sort()
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if (nums1[i] == nums2[j]) and (nums1[i] not in r):
                r.append(nums1[i])
    return r
