class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        sum=0
        m={0:1}
        for i in range(0,len(nums)):
            sum+=nums[i]
            rem=sum-k
            if rem in m:
                count+=m[rem]
            if sum in m:
                m[sum]+=1
            else:
                m[sum]=1
        return count