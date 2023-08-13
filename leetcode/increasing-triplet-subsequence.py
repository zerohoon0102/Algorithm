class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        result = False
        if len(nums) >= 3:
            first, second = nums[0], 2**31-1
            for v in nums:
                if v < first:
                    first = v
                elif v > first:
                    if v <= second:
                        second = v
                    else:
                        result = True
                        break
                    
        return result
