import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M, D = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(N)]
total = 0
for t in board:
    total += sum(t)
    
target = [[] for _ in range(M)]

for i in range(M):
    for j in range(N):
        can = deque([])
        chk = [[True]*M for i in range(N)]
        queue = deque([(N-1-j, i, 1)])
        chk[N-1-j][i] = False
        while queue:
            r, c, d = queue.popleft()
            if board[r][c]:
                can.append((r,c))
            if d < D:
                if c > 0:
                    if chk[r][c-1]:
                        queue.append((r, c-1, d+1))
                        chk[r][c-1] = False
                if r > 0:
                    if chk[r-1][c]:
                        queue.append((r-1, c, d+1))
                        chk[r-1][c] = False
                if c < M-1:
                    if chk[r][c+1]:
                        queue.append((r, c+1, d+1))
                        chk[r][c+1] = False
        target[i].append(can)

result = 0
for arr in combinations(range(M), 3):
    cur = 0
    tmp_board = [board[i].copy() for i in range(N)]
    for i in range(N):
        kill = set([])
        for m in arr:
            for r,c in target[m][i]:
                if tmp_board[r][c]:
                    kill.add((r,c))
                    break
        for r,c in kill:
            cur += 1
            tmp_board[r][c] = 0
    result = max(result, cur)
print(result)
    
# https://www.acmicpc.net/problem/17135