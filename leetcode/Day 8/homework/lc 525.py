class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {0: -1}
        max_len = count = 0
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in seen:
                max_len = max(max_len, i - seen[count])
            else:
                seen[count] = i
        return max_len