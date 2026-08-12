class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m={}
        for k in nums1:
                if k in nums2:
                    m[k]=1
        return list(m.keys())
                