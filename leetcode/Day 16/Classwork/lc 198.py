class Solution:
    def rob(self,nums: List[int]) -> int:
        n=len(nums)
        # Edge cases
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        ans =[0]*len(nums)
        ans[0]=nums[0]
        ans[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            ans[i]=max(ans[i-1],nums[i]+ans[i-2])
        return ans[-1]