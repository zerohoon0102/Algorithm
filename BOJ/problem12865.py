import sys
from collections import deque

input = sys.stdin.readline    

N, K = map(int, input().rstrip().split())
arr = [tuple(map(int, input().rstrip().split())) for _ in range(N)]

result = [-1]*(K+1)
result[0] = 0
for w, v in arr:
    for i in range(K, w-1, -1):
        if result[i-w] > -1:
            result[i] = max(result[i-w]+v, result[i])
            print(result)

print(max(result))
