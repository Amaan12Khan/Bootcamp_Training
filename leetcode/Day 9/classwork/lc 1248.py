class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left=0
        odd_count=0
        nice_subarrays=0
        current_valid_starts=0
        for right in range(len(nums)):
            if nums[right]%2!=0:
                odd_count+=1
                current_valid_starts=0
            while odd_count==k:
                current_valid_starts+=1
                if nums[left]%2!=0:
                    odd_count-=1
                left+=1
            nice_subarrays+=current_valid_starts
        return nice_subarrays