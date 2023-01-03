import sys
from collections import deque, defaultdict
from heapq import heapify, heappush, heappop
from itertools import combinations

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, S = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
queue = deque([])
result = 100001
cur = 0
cur_len = 0
for v in arr:
    cur += v
    cur_len += 1
    queue.append(v)
    if cur >= S:
        while cur - queue[0] >= S:
            cur -= queue.popleft()
            cur_len -= 1
        result = min(result, cur_len)
if result == 100001:
    print(0)
else:
    print(result)
