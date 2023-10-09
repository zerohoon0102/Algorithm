import heapq
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        INF = 10**9+1
        minNums = [INF]*n

        minNum = INF
        for idx, v in enumerate(nums):
            if v < minNum:
                minNum = v
            minNums[idx] = minNum
        
        
        revMinNums = [INF]*n
        minHeap = []
        for idx in range(n-1, -1, -1):
            while minHeap and minHeap[0] <= minNums[idx-2]:
                heapq.heappop(minHeap)
            v = nums[idx]
            if v > minNums[idx-2]:
                heapq.heappush(minHeap, v)
            
            if minHeap:
                revMinNums[idx] = minHeap[0]
            else:
                revMinNums[idx] = INF
        
        for j in range(1, n-1):
            i = minNums[j-1]
            k = revMinNums[j+1]
            if i < k < nums[j]:
                return True

        return False
