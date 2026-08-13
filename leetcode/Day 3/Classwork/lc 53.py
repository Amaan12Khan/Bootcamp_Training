class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''sum=0
        mv=nums[0]
        for v in nums:
            sum+=v
            mv=max(mv,sum)
            if sum<0:
                sum=0
        return mv'''
        curr=nums[0]
        maxi=nums[0]
        for i in range(1,len(nums)):
            curr=max(nums[i],nums[i]+curr)
            maxi=max(maxi,curr)
        return maxi