import heapq
from collections import defaultdict
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        heap = []
        count = defaultdict(int)
        for i in range(k):
            heapq.heappush(heap, -nums[i])
            count[-nums[i]] += 1
        result.append(-heap[0])
        
        i = k
        while i < len(nums):
            count[-nums[i-k]] -= 1
            heapq.heappush(heap, -nums[i])
            count[-nums[i]] += 1
            while count[heap[0]] == 0:
                heapq.heappop(heap)
            result.append(-heap[0])
            i += 1
        
        return result
