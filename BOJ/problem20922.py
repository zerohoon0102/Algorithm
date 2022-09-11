import sys
from collections import deque

input = sys.stdin.readline    

N, K = map(int,input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
num = {i:0 for i in arr}

queue = deque([])
result = 0
cur = 0
for i in arr:
    queue.append(i)
    num[i] += 1
    cur += 1
    if num[i] > K:
        result = max(result, cur-1)
        while num[i] > K:
            v = queue.popleft()
            num[v] -= 1
            cur -= 1
result = max(result, cur)
print(result)