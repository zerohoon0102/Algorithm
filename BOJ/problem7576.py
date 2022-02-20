import sys
from collections import deque

M, N = map(int, sys.stdin.readline().rstrip().split())

box = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

queue = deque([])
tomato = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i,j))
            tomato -= 1
        if box[i][j] != -1:
            tomato += 1

y = [0,0,1,-1]
x = [1,-1,0,0]

delay = 0
while queue and (tomato > 0):
    for _ in range(len(queue)):
        i, j = queue.popleft()
        for k in range(4):
            if 0 <= i+y[k] < N and 0 <= j+x[k] < M:
                if box[i+y[k]][j+x[k]] == 0:
                    box[i+y[k]][j+x[k]] = 1
                    tomato -= 1
                    queue.append((i+y[k], j+x[k]))
    delay += 1
            
if tomato > 0:
    print(-1)
else:
    print(delay)          
        
