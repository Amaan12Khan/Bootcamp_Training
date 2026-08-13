class Solution:
    def fib(self, n: int,mp={}) -> int:
        # Base case
        if n <= 1:
            return n
        if n in mp:
            return mp[n]
        x = self.fib(n - 1, mp)
        y = self.fib(n - 2, mp)
        mp[n] = x + y
        return mp[n]