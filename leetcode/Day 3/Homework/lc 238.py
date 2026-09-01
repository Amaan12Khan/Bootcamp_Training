class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        P = [1] * n   
        su = [1] * n
        a=[]
        for i in range(1,len(nums)):
            P[i]=P[i-1]*nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            su[j]=nums[j+1]*su[j+1]
        for x in range(len(nums)):
            a.append(P[x]*su[x])
        return a