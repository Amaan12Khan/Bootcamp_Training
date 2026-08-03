class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth=0
        for i in accounts:
            sums=0
            for j in i:
                sums=sums+j   
            if sums>max_wealth:
                    max_wealth=sums
        return max_wealth
#time complexity=O(n*m)
#space complexity=O(1)