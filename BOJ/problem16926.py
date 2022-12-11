import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M, R = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(N)]
sub_board = [arr.copy() for arr in board]

T = min(M, N) // 2

for t in range(T):
    i,j = t,t
    n = N - t*2
    m = M - t*2
    rep = 2*(m + n) - 4
    rep = R%rep
    while rep:
        if i == t + n-1:
            # bottom
            if j == t + m-1:
                if rep >= n-1:
                    i = t
                    rep -= n-1
                else:
                    i -= rep
                    rep = 0
            else:
                if rep >= m-1:
                    j = t + m-1
                    rep -= m-1
                else:
                    j += rep
                    rep = 0
        elif i == t:
            # top
            if j == t:
                if rep >= n-1:
                    i = t + n-1
                    rep -= n-1
                else:
                    i += rep
                    rep = 0
            else:
                if rep >= m-1:
                    j = t
                    rep -= m-1
                else:
                    j -= rep
                    rep = 0
    board[i][j] = sub_board[t][t]
    v_i, v_j = t+1,t
    while v_i != t or v_j != t:
        if i == t + n-1:
            if j == t + m-1:
                i -= 1
            else:
                j += 1
        elif i == t:
            if j == t:
                i += 1
            else:
                j -= 1
        else:
            if j == t:
                i += 1
            else:
                i -= 1
        board[i][j] = sub_board[v_i][v_j]
        
        if v_i == t + n-1:
            if v_j == t + m-1:
                v_i -= 1
            else:
                v_j += 1
        elif v_i == t:
            if v_j == t:
                v_i += 1
            else:
                v_j -= 1
        else:
            if v_j == t:
                v_i += 1
            else:
                v_i -= 1
    
for arr in board:
    print(' '.join(map(str, arr)))
    
