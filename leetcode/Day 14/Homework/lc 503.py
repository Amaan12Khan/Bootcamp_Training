class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        size=len(nums)
        ans=[0]*size

        for index in range(size -1,-1,-1):
            data=nums[index]

            while stack:
                if stack[-1]>data:
                    ans[index]=stack[-1]
                    break
                else:
                    stack.pop()

            if not stack:
                ans[index]=-1
            stack.append(data)

        for index in range(size -1,-1,-1):
            data=nums[index]

            while stack:
                if stack[-1]>data:
                    ans[index]=stack[-1]
                    break
                else:
                    stack.pop()

            if not stack:
                ans[index]=-1
            stack.append(data)

        return ans