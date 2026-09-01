class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0: return False
        target = sum(nums) // 2
        dp = set([0])
        for n in nums:
            nextDp = set(dp)
            for t in dp:
                if t + n == target: return True
                nextDp.add(t + n)
            dp = nextDp
        return target in dp