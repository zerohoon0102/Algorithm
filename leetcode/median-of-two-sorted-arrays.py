class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        median = (n+m)//2

        i, j = 0, 0
        v = 0
        prev_v = 0
        while i < n or j < m:
            if i < n and j < m:
                if nums1[i] <= nums2[j]:
                    v = nums1[i]
                    i += 1
                else:
                    v = nums2[j]
                    j += 1
            elif i < n:
                v = nums1[i]
                i += 1
            elif j < m:
                v = nums2[j]
                j += 1
            
            if i+j == median:
                prev_v = v
            if i+j == median + 1:
                if (n+m)%2 == 1:
                    return v
                else:
                    return (v + prev_v)/2
