import sys

N = 19
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

result = 0

def chk():
    count = [0,0]
    for j in range(N):
        i = 0
        while i < N:
            s = board[j][i]
            if s == 0:
                count[0] = 0
                count[1] = 0
            else:
                for t in range(2):
                    if s == t+1:
                        count[t] += 1
                        count[abs(t-1)] = 0
                        if count[t] == 5:
                            if i == N-1 or (i < N-1 and board[j][i+1] != t+1):
                                return (t+1, j, i-4)
            i += 1
        count = [0,0]
        
        i = 0
        while i < N:
            s = board[i][j]
            if s == 0:
                count[0] = 0
                count[1] = 0
            else:
                for t in range(2):
                    if s == t+1:
                        count[t] += 1
                        count[abs(t-1)] = 0
                        if count[t] == 5:
                            if i == N-1 or (i < N-1 and board[i+1][j] != t+1):
                                return (t+1, i-4, j)
            i += 1
        count = [0,0]

        i = 0
        k = j
        while i < N and k < N:
            s = board[i][k]
            if s == 0:
                count[0] = 0
                count[1] = 0
            else:
                for t in range(2):
                    if s == t+1:
                        count[t] += 1
                        count[abs(t-1)] = 0
                        if count[t] == 5:
                            if i == N-1 or k == N-1 or (i < N-1 and k < N-1 and board[i+1][k+1] != t+1):
                                return (t+1, i-4, k-4)
            i += 1
            k += 1

        count = [0,0]

        i = 0
        k = j
        while i < N and k < N:
            s = board[k][i]
            if s == 0:
                count[0] = 0
                count[1] = 0
            else:
                for t in range(2):
                    if s == t+1:
                        count[t] += 1
                        count[abs(t-1)] = 0
                        if count[t] == 5:
                            if i == N-1 or k == N-1 or (i < N-1 and k < N-1 and board[k+1][i+1] != t+1):
                                return (t+1, k-4, i-4)
            i += 1
            k += 1

        i = N-1
        k = j
        count = [0,0]
        while i >= 0 and N > k:
            s = board[i][k]
            if s == 0:
                count[0] = 0
                count[1] = 0
            else:
                for t in range(2):
                    if s == t+1:
                        count[t] += 1
                        count[abs(t-1)] = 0
                        if count[t] == 5:
                            if i == 0 or k == N-1 or (i > 0 and k < N-1 and board[i-1][k+1] != t+1):
                                return (t+1, i+4, k-4)
            i -=1
            k += 1

        i = 0
        k = j
        count = [0,0]
        while N > i and k >= 0:
            s = board[k][i]
            if s == 0:
                count[0] = 0
                count[1] = 0
            else:
                for t in range(2):
                    if s == t+1:
                        count[t] += 1
                        count[abs(t-1)] = 0
                        if count[t] == 5:
                            if i == N-1 or k == 0 or (i < N-1 and k > 0 and board[k-1][i+1] != t+1):
                                return (t+1, k+4, i-4)
            k -= 1
            i += 1
        count = [0,0]
    return 0
        

result = chk()
if result == 0:
    print(0)
else:
    print(result[0])
    print(result[1]+1, result[2]+1)
