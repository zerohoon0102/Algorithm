import sys
from collections import deque, defaultdict
import heapq

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

NONE = 100001
N, M, X = map(int, input().rstrip().split())
roads = [{} for _ in range(N)]
reverse_roads = [{} for _ in range(N)]
for _ in range(M):
    s, e, t = map(int, input().rstrip().split())
    roads[s-1][e-1] = t
    reverse_roads[e-1][s-1] = t
x = X-1

info = [NONE]*N
info[x] = 0
chk = [1]*N
rest = N

heap = [(0, x)]
while rest > 0:
    value, idx = heapq.heappop(heap)
    if chk[idx] == 0:
        continue
    chk[idx] = 0
    rest -= 1
    for nxt in roads[idx]:
        if chk[nxt] == 0:
            continue
        info[nxt] = min(info[nxt], info[idx] + roads[idx][nxt])
        heapq.heappush(heap, (info[nxt], nxt))

rev_info = [NONE]*N
chk = [1]*N
rest = N
heap = [(0, x)]
roads = reverse_roads
rev_info[x] = 0
while rest > 0:
    value, idx = heapq.heappop(heap)
    if chk[idx] == 0:
        continue
    chk[idx] = 0
    rest -= 1
    for nxt in roads[idx]:
        if chk[nxt] == 0:
            continue
        rev_info[nxt] = min(rev_info[nxt], rev_info[idx] + roads[idx][nxt])
        heapq.heappush(heap, (rev_info[nxt], nxt))

result = 0
for i in range(N):
    result = max(result, info[i]+rev_info[i])
print(result)
