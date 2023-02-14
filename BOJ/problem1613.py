import sys
from collections import deque, defaultdict
from heapq import heapify, heappush, heappop
from itertools import combinations

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
chk = [[True]*n for _ in range(n)]
dp = [[1]*n for _ in range(n)]

result = 0
direc_x = [0, 0, 1, -1]
direc_y = [1, -1, 0, 0]
def dfs(x, y):
    if not chk[x][y]:
        return dp[x][y]
    value = 1
    chk[x][y] = False
    for i in range(4):
        nxt_x = x + direc_x[i]
        nxt_y = y + direc_y[i]
        if 0 <= nxt_x < n and 0 <= nxt_y < n:
            if arr[x][y] < arr[nxt_x][nxt_y]:
                value = max(value, dfs(nxt_x, nxt_y) + 1)
    dp[x][y] = value
    return value
for h in range(n):
    for w in range(n):
        result = max(result, dfs(h, w))
        
print(result)
