class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum=0
        current_sum=0
        window_counts={}
        left=0
        for right in range(len(nums)):
            num=nums[right]
            current_sum+=num
            window_counts[num]=window_counts.get(num,0)+1
            if right-left+1 > k:
                left_num=nums[left]
                current_sum-=left_num
                window_counts[left_num]-=1
                if window_counts[left_num]==0:
                    del window_counts[left_num]
                left+=1
            if right-left+1==k and len(window_counts)==k:
                max_sum=max(max_sum, current_sum)
        return max_sum