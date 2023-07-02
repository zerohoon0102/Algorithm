import sys
from collections import deque
import heapq

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())
cost_water = []
for i in range(N):
    heapq.heappush(cost_water, (int(input()), i))

cost_line = []
for i in range(N):
    arr = list(map(int, input().split()))
    cost_line.append(arr)

chk_water = [1]*N
result = 0
rest = N

while rest > 0:
    cost, idx = heapq.heappop(cost_water)
    if chk_water[idx] == 0:
        continue
    chk_water[idx] = 0
    rest -= 1
    result += cost
    for i in range(N):
        if i == idx or chk_water[i] == 0:
            continue
        heapq.heappush(cost_water, (cost_line[idx][i], i))
print(result)
