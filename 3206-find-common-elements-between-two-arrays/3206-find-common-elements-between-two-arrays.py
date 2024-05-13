class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n= len(nums1)
        m = len(nums2)
        k,l=0,0

        for i in range(0,n):
            if nums1[i] in nums2:
                k+=1
        for j in range(0,m):
            if nums2[j] in nums1:
                l+=1

        return[k,l]
        