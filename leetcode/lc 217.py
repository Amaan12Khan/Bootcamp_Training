class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m={}
        for k in nums:
            if k in m:
                return True
            m[k]=1
        return False
