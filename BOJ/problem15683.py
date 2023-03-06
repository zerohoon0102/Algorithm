import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

arr = []
cctvs = []
zero = 0
direc_y = [-1,0,1,0]
direc_x = [0,1,0,-1]

for i in range(N):
    line = list(map(int, input().rstrip().split()))
    arr.append(line)
    for j, v in enumerate(line):
        if v == 0:
            zero += 1
        elif v < 6:
            cctvs.append((i,j,v))
result = zero

def copy(board):
    new = []
    for tmp in board:
        new.append(tmp.copy())
    return new

def dfs(board, idx, value):
    global result
    i, j, v = cctvs[idx]
    if v == 1:
        for d in range(4):
            nxt_board = copy(board)
            nxt_value = value
            nxt_i = i + direc_y[d]
            nxt_j = j + direc_x[d]
            while 0 <= nxt_i < N and 0 <= nxt_j < M and nxt_board[nxt_i][nxt_j] != 6:
                if nxt_board[nxt_i][nxt_j] == 0:
                    nxt_board[nxt_i][nxt_j] = -1
                    nxt_value -= 1
                nxt_i += direc_y[d]
                nxt_j += direc_x[d]
            if idx < len(cctvs)-1:
                dfs(nxt_board, idx+1, nxt_value)
            else:
                result = min(result, nxt_value)
    elif v == 2:
        for d in range(2):
            nxt_board = copy(board)
            nxt_value = value
            for case in range(0, 3, 2):
                nxt_i = i + direc_y[d+case]
                nxt_j = j + direc_x[d+case]
                while 0 <= nxt_i < N and 0 <= nxt_j < M and nxt_board[nxt_i][nxt_j] != 6:
                    if nxt_board[nxt_i][nxt_j] == 0:
                        nxt_board[nxt_i][nxt_j] = -1
                        nxt_value -= 1
                    nxt_i += direc_y[d+case]
                    nxt_j += direc_x[d+case]
            if idx < len(cctvs)-1:
                dfs(nxt_board, idx+1, nxt_value)
            else:
                result = min(result, nxt_value)
    elif v == 3:
        for d in range(4):
            nxt_board = copy(board)
            nxt_value = value
            for case in range(0, -2, -1):
                nxt_i = i + direc_y[d+case]
                nxt_j = j + direc_x[d+case]
                while 0 <= nxt_i < N and 0 <= nxt_j < M and nxt_board[nxt_i][nxt_j] != 6:
                    if nxt_board[nxt_i][nxt_j] == 0:
                        nxt_board[nxt_i][nxt_j] = -1
                        nxt_value -= 1
                    nxt_i += direc_y[d+case]
                    nxt_j += direc_x[d+case]
            if idx < len(cctvs)-1:
                dfs(nxt_board, idx+1, nxt_value)
            else:
                result = min(result, nxt_value)
    elif v == 4:
        for d in range(4):
            nxt_board = copy(board)
            nxt_value = value
            for case in range(0, -3, -1):
                nxt_i = i + direc_y[d+case]
                nxt_j = j + direc_x[d+case]
                while 0 <= nxt_i < N and 0 <= nxt_j < M and nxt_board[nxt_i][nxt_j] != 6:
                    if nxt_board[nxt_i][nxt_j] == 0:
                        nxt_board[nxt_i][nxt_j] = -1
                        nxt_value -= 1
                    nxt_i += direc_y[d+case]
                    nxt_j += direc_x[d+case]
            if idx < len(cctvs)-1:
                dfs(nxt_board, idx+1, nxt_value)
            else:
                result = min(result, nxt_value)
        
    elif v == 5:
        for d in range(4):
            nxt_i = i + direc_y[d]
            nxt_j = j + direc_x[d]
            while 0 <= nxt_i < N and 0 <= nxt_j < M and board[nxt_i][nxt_j] != 6:
                if board[nxt_i][nxt_j] == 0:
                    board[nxt_i][nxt_j] = -1
                    value -= 1
                nxt_i += direc_y[d]
                nxt_j += direc_x[d]
        if idx < len(cctvs)-1:
            dfs(board, idx+1, value)
        else:
            result = min(result, value)
if cctvs:
    dfs(arr, 0, result)

print(result)
