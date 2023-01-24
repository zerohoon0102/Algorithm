import sys
from collections import deque, defaultdict
from heapq import heapify, heappush, heappop
from itertools import combinations

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())
time = [0]*(N+1)
dp = [0]*(N+1)
pre = [0]*(N+1)
path = [[] for _ in range(N+1)]

queue = deque([])

for i in range(N):
    values = list(map(int, input().rstrip().split()))
    time[i+1] = values[0]
    p = values[1]
    if p == 0:
        queue.append(i+1)
        dp[i+1] = time[i+1]
    else:
        pre[i+1] = p
        for j in values[2:]:
            path[j].append(i+1)

while queue:
    cur = queue.popleft()
    for nxt in path[cur]:
        pre[nxt] -= 1
        if pre[nxt] == 0:
            queue.append(nxt)
        dp[nxt] = max(dp[nxt], dp[cur]+time[nxt])

print(max(dp))
