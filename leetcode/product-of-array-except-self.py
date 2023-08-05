class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)

        cur_value = 1
        for i, v in enumerate(nums):
            cur_value *= v
            prefix[i] = cur_value
        
        cur_value = 1
        for i in range(len(nums)-1, -1, -1):
            v = nums[i]
            cur_value *= v
            suffix[i] = cur_value
        
        result = []
        for i in range(len(nums)):
            if 0 < i < len(nums)-1:
                result.append(prefix[i-1]*suffix[i+1])
            elif i == 0:
                result.append(suffix[i+1])
            else:
                result.append(prefix[i-1])
        return result