class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = nums
        for i,v in enumerate(dp):
            if i > 2:
                dp[i] = max(dp[i-2], dp[i-3])+v
            elif i == 2:
                dp[i] = dp[i]+dp[i-2]
        return max(dp)
