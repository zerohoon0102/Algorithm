from collections import deque
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    queue =deque([[0,0,1]])
    frame = [[10000]*m for _ in range(n)]
    frame[0][0] = 1
    while(queue):
        i, j, mon = queue.popleft()
        if (i < n-1) and (maps[i+1][j] == 1) and (frame[i+1][j] > mon+1):
            frame[i+1][j] = mon+1
            queue.append([i+1, j, mon+1])
        if (i > 0) and (maps[i-1][j] == 1) and (frame[i-1][j] > mon+1):
            frame[i-1][j] = mon+1
            queue.append([i-1, j, mon+1])
        if (j < m-1) and (maps[i][j+1] == 1) and (frame[i][j+1] > mon + 1):
            frame[i][j+1] = mon+1
            queue.append([i, j+1, mon+1])
        if (j > 0) and (maps[i][j-1] == 1) and (frame[i][j-1] > mon + 1):
            frame[i][j-1] = mon+1
            queue.append([i, j-1, mon+1])
    if frame[n-1][m-1] == 10000:
        return -1
    else:
        return frame[n-1][m-1]