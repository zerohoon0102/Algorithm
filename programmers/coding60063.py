from collections import deque

def solution(board):
    answer = 0
    length = len(board)
    dp_h = [[10000]*length for _ in range(length)]
    dp_v = [[10000]*length for _ in range(length)]
    
    queue = deque([(0,0,0,True)])
    while queue:
        i,j,v,t = queue.popleft()
        #print(i,j,v,t)
        if ((i == length-1 and j == length-2 and t) or
            (i == length-2 and j == length-1 and not t)):
            return v
        if t:
            if v > dp_h[i][j]:
                continue
            if i > 0:
                if board[i-1][j] == 0 and board[i-1][j+1] == 0:
                    # 위로 한 칸 이동 및 위로 회전
                    if v+1 < dp_h[i-1][j]:
                        dp_h[i-1][j] = v+1
                        queue.append((i-1,j,v+1,True))
                    # 위 왼쪽
                    if v+1 < dp_v[i-1][j]:
                        dp_v[i-1][j] = v+1
                        queue.append((i-1,j,v+1,False))
                    # 위 오른쪽
                    if v+1 < dp_v[i-1][j+1]:
                        dp_v[i-1][j+1] = v+1
                        queue.append((i-1,j+1,v+1,False))
            if i < length-1:
                if board[i+1][j] == 0 and board[i+1][j+1] == 0:
                    # 아래로 한 칸 이동 및 아래로 회전
                    if v+1 < dp_h[i+1][j]:
                        dp_h[i+1][j] = v+1
                        queue.append((i+1,j,v+1,True))
                    # 아래 왼쪽
                    if v+1 < dp_v[i][j]:
                        dp_v[i][j] = v+1
                        queue.append((i,j,v+1,False))
                    # 아래 오른쪽
                    if v+1 < dp_v[i][j+1]:
                        dp_v[i][j+1] = v+1
                        queue.append((i,j+1,v+1,False))
            if j > 0:
                # 왼쪽으로 이동
                if board[i][j-1] == 0 and v+1 < dp_h[i][j-1]:
                    dp_h[i][j-1] = v+1
                    queue.append((i,j-1,v+1,True))
            if j < length-2:
                # 오른쪽으로 이동
                if board[i][j+2] == 0 and v+1 < dp_h[i][j+1]:
                    dp_h[i][j+1] = v+1
                    queue.append((i,j+1,v+1,True))
        else:
            if v > dp_v[i][j]:
                continue
            if j > 0:
                if board[i][j-1] == 0 and board[i+1][j-1] == 0:
                    # 왼쪽으로 이동
                    if v+1 < dp_v[i][j-1]:
                        dp_v[i][j-1] = v+1
                        queue.append((i,j-1,v+1,False))
                    # 왼쪽 위
                    if v+1 < dp_h[i][j-1]:
                        dp_h[i][j-1] = v+1
                        queue.append((i,j-1,v+1,True))
                    # 왼쪽 아래
                    if v+1 < dp_h[i+1][j-1]:
                        dp_h[i+1][j-1] = v+1
                        queue.append((i+1,j-1,v+1,True))
            if j < length-1:
                if board[i][j+1] == 0 and board[i+1][j+1] == 0:
                    # 오른쪽으로 이동
                    if v+1 < dp_v[i][j+1]:
                        dp_v[i][j+1] = v+1
                        queue.append((i,j+1,v+1,False))
                    # 오른쪽 위
                    if v+1 < dp_h[i][j]:
                        dp_h[i][j] = v+1
                        queue.append((i,j,v+1,True))
                    # 오른쪽 아래
                    if v+1 < dp_h[i+1][j]:
                        dp_h[i+1][j] = v+1
                        queue.append((i+1,j,v+1,True))
            if i > 0:
                # 위쪽으로 이동
                if board[i-1][j] == 0 and v+1 < dp_v[i-1][j]:
                    dp_v[i-1][j] = v+1
                    queue.append((i-1,j,v+1,False))
            if i < length-2:
                # 아래쪽으로 이동
                if board[i+2][j]==0 and v+1 < dp_v[i+1][j]:
                    dp_v[i+1][j] = v+1
                    queue.append((i+1,j,v+1,False))