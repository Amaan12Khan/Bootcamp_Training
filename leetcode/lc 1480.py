class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum=[]
        sums=0
        for i in nums:
            sums+=i
            runningSum.append(sums)
        return runningSum
#time complexity=O(n)
#space complexity=O(n)