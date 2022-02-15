import sys
from collections import deque

W, H = map(int, sys.stdin.readline().rstrip().split())

area = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(H)]

lock = [[True]*W for _ in range(H)]

direc = [[[0,1],[-1,1],[0,1]],
         [[-1,0], [-1,1], [-1,0]]]

result = 0
queue = deque([])
for i in range(W):
    if area[0][i] == 0:
        lock[0][i] = False
        queue.append((0,i))
    else:
        if i == W-1:
            result += 1
        else:
            result += 2
    if area[H-1][i] == 0:
        lock[H-1][i] = False
        queue.append((H-1, i))
    else:
        row = (H-1)%2
        if row == 0:
            if i == W-1:
                result += 1
            else:
                result += 2
        else:
            if i == 0:
                result += 1
            else:
                result += 2

for i in range(H):
    row = i%2
    if area[i][0] == 0:
        if lock[i][0]:
            lock[i][0] = False
            queue.append((i,0))
    else:
        if row == 0:
            result += 1
        else:
            result += 3
    if area[i][W-1] == 0:
        if lock[i][W-1]:
            lock[i][W-1] = False
            queue.append((i, W-1))
    else:
        if row == 0:
            result += 3
        else:
            result += 1

while queue:
    i,j = queue.popleft()
    row = i%2
    for h in range(3):
        for w in direc[row][h]:
            nxt_i = i+h-1
            nxt_j = j+w
            if nxt_i < 0 or nxt_i >= H or nxt_j < 0 or nxt_j >= W:
                continue
            if not area[nxt_i][nxt_j]:
                if lock[nxt_i][nxt_j]:
                    queue.append((nxt_i, nxt_j))
                    lock[nxt_i][nxt_j] = False
            else:
                result += 1

print(result)

"""
import sys
from collections import deque

W, H = map(int, sys.stdin.readline().rstrip().split())

area = [[0]*(W+2)]
for _ in range(H):
    arr = [0]
    arr.extend(list(map(int, sys.stdin.readline().rstrip().split())))
    arr.append(0)
    area.append(arr)
area.append([0]*(W+2))

lock = [[True]*(W+2)]
for _ in range(H):
    arr = [True]
    arr.extend([False]*W)
    arr.append(True)
    lock.append(arr)
lock.append([True]*(W+2))

queue = deque([])
for i in range(1, W+1):
    if area[1][i] == 0:
        lock[1][i] = True
        queue.append((1,i))
    if area[H][i] == 0:
        lock[H][i] = True
        queue.append((H, i))

for i in range(2, H):
    if area[i][1] == 0:
        lock[i][1] = True
        queue.append((i,1))
    if area[i][W] == 0:
        lock[i][W] = True
        queue.append((i, W))

direc = [[[-1,0], [-1,1], [-1,0]],
         [[0,1],[-1,1],[0,1]]]

while queue:
    i,j = queue.popleft()
    row = i%2
    for h in range(3):
        for w in direc[row][h]:
            if not (area[i+h-1][j+w] or lock[i+h-1][j+w]):
                queue.append((i+h-1, j+w))
                lock[i+h-1][j+w] = True

result = 0
for i in range(1, H+1):
    row = i%2
    for j in range(1, W+1):
        if area[i][j]:
            for h in range(3):
                for w in direc[row][h]:
                    if lock[i+h-1][j+w]:
                        result += 1

print(result)          
        
"""