class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_minus = -1000000
        ans = 0
        cnt = 0
        for i in range(len(nums)):
            cnt += nums[i]
            if cnt > ans:
                ans = cnt
            if cnt < 0:
                cnt = 0
            if nums[i] > max_minus and nums[i] <= 0:
                max_minus = nums[i]
        if ans == 0:
            return max_minus
        return ans