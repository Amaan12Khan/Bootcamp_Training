class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def helper(arr):
            a, b = 0, 0
            for n in arr:
                a, b = b, max(a + n, b)
            return b
        return max(helper(nums[1:]), helper(nums[:-1]))