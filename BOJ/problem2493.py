import sys
import heapq

N = int(sys.stdin.readline().rstrip())

tower = list(map(int, sys.stdin.readline().rstrip().split()))
heap = []
result = ["" for _ in range(N)]

for i in range(N-1, -1, -1):
    num = tower[i]
    while(heap):
        if heap[0][0] <= num:
            min_num, min_idx = heapq.heappop(heap)
            result[min_idx] = str(i+1)
        else:
            break
    heapq.heappush(heap, [num, i])
    
for src in heap:
    result[src[1]] = "0"

print(" ".join(result))
