
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minValue = maxValue = ans = nums[0]
        for i in range(1,len(nums)):
            data = nums[i]
            tempMin = min(data, minValue * data, maxValue * data)
            tempMax = max(data, minValue * data, maxValue * data)
            minValue, maxValue = tempMin, tempMax

            ans = max(ans, maxValue)
        return ans
            