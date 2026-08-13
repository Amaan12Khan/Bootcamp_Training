class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = 0
        curr_max_sum = 0
        curr_min_sum = 0
        max_sum = float('-inf')
        min_sum = float('inf')
        
        for num in nums:
            total_sum += num
            
            # Standard Kadane's to find max subarray
            curr_max_sum = max(curr_max_sum + num, num)
            max_sum = max(max_sum, curr_max_sum)
            
            # Modified Kadane's to find min subarray
            curr_min_sum = min(curr_min_sum + num, num)
            min_sum = min(min_sum, curr_min_sum)
            
        # Edge Case: If all elements are negative, total_sum - min_sum equals 0.
        # But an empty subarray isn't allowed, so we must return the largest single negative value.
        if max_sum < 0:
            return max_sum
            
        # Return the best choice between the straight middle or the wrapping edges
        return max(max_sum, total_sum - min_sum)