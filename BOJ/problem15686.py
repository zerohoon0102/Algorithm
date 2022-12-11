import sys
from collections import deque, defaultdict
from heapq import heapify, heappush, heappop
from itertools import combinations

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(N)]
home = []
shop = []
chk = {}
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            home.append((i,j))
        elif board[i][j] == 2:
            shop.append((i,j))
            chk[(i,j)] = True

chicken = {}
for h in home:
    chicken[h] = []
    for s in shop:
        chicken[h].append((s[0],s[1], abs(s[0]-h[0])+abs(s[1]-h[1])))
    chicken[h].sort(key=lambda x: x[2])

result = 100000000
for arr in combinations(range(len(shop)), len(shop)-M):
    tmp = chk.copy()
    for v in arr:
        tmp[shop[v]] = False
    cur = 0
    for i_h, j_h in home:
        for s in chicken[(i_h,j_h)]:
            s0, s1, value = s
            if tmp[(s0, s1)]:
                cur += value
                break
    result = min(result, cur)
print(result)
