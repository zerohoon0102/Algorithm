import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
point = []
for _ in range(N-1):
    point.append(list(map(int, sys.stdin.readline().rstrip().split())))

K = int(sys.stdin.readline().rstrip())

result = 100000

def dfs(idx, chk, score):
    global result
    if idx == N-1:
        if result > score:
            result = score
    else:
        if idx + 1 < N:
            dfs(idx + 1, chk, score+point[idx][0])
            if idx + 2 < N:
                dfs(idx + 2, chk, score+point[idx][1])
                if idx + 3 < N and chk:
                    dfs(idx + 3, False, score+K)

dfs(0, True, 0)

print(result)
