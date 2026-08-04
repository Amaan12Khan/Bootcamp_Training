class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[0]*(2*n)
        '''for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])'''
        for i in range(0,n):
            ans[2*i]=nums[i]
            ans[2*i+1]=nums[i+n]
        return ans