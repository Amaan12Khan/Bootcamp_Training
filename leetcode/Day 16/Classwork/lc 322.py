class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=dict()
        def f(nums, ind, amount):
            if amount == 0:
                return 0
            if ind >= len(coins):
                return 999999
            if (ind,amount) in dp:
                return dp[(ind,amount)]
            skip = f(nums, ind + 1, amount)
            take = 999999
            if amount>=coins[ind]:
                take = 1 + f(nums, ind, amount - nums[ind])
            dp[(ind,amount)]=min(take, skip)
            return dp[(ind,amount)]
        ans = f(coins, 0, amount)
        if ans > amount:
            return -1
        return ans