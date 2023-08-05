class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)

        cur_value = 1
        for i, v in enumerate(nums):
            result[i] = cur_value
            cur_value *= nums[i]
        
        cur_value = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= cur_value
            cur_value *= nums[i]
        
        return result