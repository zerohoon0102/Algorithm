import sys
from collections import deque

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M, T = map(int, input().rstrip().split())
board = [0]
result = 0
rest = M*N
direc_i = [0,0,1,-1]
direc_j = [1,-1,0,0]

for _ in range(N):
    arr = deque(map(int, input().rstrip().split()))
    result += sum(arr)
    board.append(arr)

chk = None
def dfs(i, j, remove):
    global result, rest
    for k in range(4):
        nxt_i = i + direc_i[k]
        nxt_j = j + direc_j[k]
        if nxt_j >= M:
            nxt_j %= M
        if nxt_j < 0:
            nxt_j = M-1
        if 0 < nxt_i <= N:
            if chk[nxt_i][nxt_j] and board[nxt_i][nxt_j]:
                if board[i][j] == board[nxt_i][nxt_j]:
                    remove = True
                    chk[nxt_i][nxt_j] = False
                    dfs(nxt_i, nxt_j, remove)
    
    if remove:
        result -= board[i][j]
        board[i][j] = 0
        rest -= 1

for _ in range(T):
    base_x, d, k = map(int, input().rstrip().split())
    x = base_x
    while x <= N:  
        arr = board[x]
        if d == 0:
            for _ in range(k):
                v = arr.pop()
                arr.appendleft(v)
        else:
            for _ in range(k):
                v = arr.popleft()
                arr.append(v)
        x += base_x
    chk = [[True]*M for _ in range(N+1)]
    bef_rest = rest
    for y in range(1, N+1):
        for x in range(M):
            if chk[y][x] and board[y][x]:
                chk[y][x] = False
                dfs(y, x, False)
    bef_result = result
    
    if bef_rest == rest:
        for y in range(1, N+1):
            for x in range(M):
                if 0 < board[y][x]:
                    if board[y][x] < bef_result/rest:
                        board[y][x] += 1
                        result += 1
                    elif board[y][x] > bef_result/rest:
                        board[y][x] -= 1
                        result -= 1
print(result)
