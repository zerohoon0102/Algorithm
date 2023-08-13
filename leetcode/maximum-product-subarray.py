from collections import deque
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minus = None
        result = -10
        
        i = 0
        cur_value = 1
        while i < len(nums):
            cur_value *= nums[i]
            if cur_value < 0:
                if minus:
                    result = max(result, cur_value//minus)
                else:
                    result = max(result, cur_value)
                if minus == None:
                    minus = cur_value
            elif cur_value == 0:
                result = max(result, 0)
                cur_value = 1
                minus = None
            else:
                result = max(result, cur_value)
            i += 1
        
        return result
