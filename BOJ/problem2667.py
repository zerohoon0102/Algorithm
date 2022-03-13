import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

board = [sys.stdin.readline().rstrip() for _ in range(N)]
chk_board = [[True]*N for _ in range(N)]

queue = deque([])
rest = N*N

for i in range(N):
    for j in range(N):
        if board[i][j] == '0':
            chk_board[i][j] = False
            rest -= 1
        else:
            if len(queue) == 0:
                queue.append((i,j))
                chk_board[i][j] = False

result = []
while 1:
    count = 0
    while queue:
        i, j = queue.popleft()
        count += 1
        rest -= 1
        if i > 0 and chk_board[i-1][j]:
            queue.append((i-1, j))
            chk_board[i-1][j] = False
        if i < N-1 and chk_board[i+1][j]:
            queue.append((i+1, j))
            chk_board[i+1][j] = False
        if j > 0 and chk_board[i][j-1]:
            queue.append((i, j-1))
            chk_board[i][j-1] = False
        if j < N-1 and chk_board[i][j+1]:
            queue.append((i, j+1))
            chk_board[i][j+1] = False
    result.append(count)
    if rest == 0:
        break
    for i in range(N):
        for j in range(N):
            if chk_board[i][j]:
                queue.append((i,j))
                chk_board[i][j] = False
                break
        if queue:
            break

print(len(result))
result.sort()
for s in result:
    print(s)
