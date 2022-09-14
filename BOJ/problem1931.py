import sys
sys.setrecursionlimit(1000000)
from collections import deque

input = sys.stdin.readline    

N = int(input().rstrip())
arr = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[0]))

result = 0
right = 0
for start, end in arr:
    if start < right:
        continue
    right = end
    result += 1
print(result)
