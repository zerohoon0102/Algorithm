class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        result = 0
        
        for i, num in enumerate(nums):
            cur_length = self.getNum(dp, num, 1, result)
            if cur_length in dp:
                dp[cur_length] = min(num, dp[cur_length])
            else:
                dp[cur_length] = num
                result = cur_length
        return result
    
    def getNum(self, dp, num, s, e):
        mid = (s+e)//2
        result = 1
        while s < e:
            if dp[mid] < num:
                s = mid+1
            elif dp[mid] > num:
                e = mid
            else:
                break
            mid = (s+e)//2
        
        if mid-1 in dp:
            if dp[mid-1] < num <= dp[mid]:
                result = mid
            else:
                result = mid+1
        elif mid in dp:
            if dp[mid] < num:
                result = mid + 1
            else:
                result = mid
        
        return result