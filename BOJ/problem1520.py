import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

M, N = map(int, input().rstrip().split())
table = [list(map(int, input().rstrip().split())) for _ in range(M)]
chk = [[[-1]*4 for _ in range(N)] for _ in range(M)]
ver = [-1, 1, 0, 0]
hor = [0, 0, -1, 1]

# Top, Bottom, Left, Right
result = 0
def dfs(i, j):
    global result
    if i == M-1 and j == N-1:
        return 1
    cur_result = 0
    for idx, v in enumerate(chk[i][j]):
        if v != -1:
            cur_result += v
        else:
            nxt_i = i+ver[idx]
            nxt_j = j+hor[idx]
            if (0 <= nxt_i <= M-1 and 0 <= nxt_j <= N-1 and
                table[nxt_i][nxt_j] < table[i][j]):
                cur = dfs(nxt_i, nxt_j)
                chk[i][j][idx] = cur
                cur_result += cur
    
    return cur_result

result = dfs(0,0)
print(result)
