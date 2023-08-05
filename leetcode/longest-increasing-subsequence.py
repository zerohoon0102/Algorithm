class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        result = 0
        
        for i, num in enumerate(nums):
            cur_length = 1
            for j in range(result, 0, -1):
                if dp[j] < num:
                    cur_length = j + 1
                    break
            if cur_length in dp:
                dp[cur_length] = min(num, dp[cur_length])
            else:
                dp[cur_length] = num
            result = max(result, cur_length)
        return result
