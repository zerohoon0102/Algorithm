from collections import deque     

def solution(board):
    length = len(board)
    def bfs(x,y,cost,direc):
        min_dist = [[200000000]*length for _ in range(length)]
        queue = deque([[x,y, cost, direc]])
        min_dist[0][0] = 0
        while(len(queue) != 0):
            i, j, cost, direc = queue.popleft()
            if (i+1 < length) and (board[i+1][j] == 0):
                tmp_cost = cost+600 if direc != 'v' else cost+100
                if min_dist[i+1][j] >= tmp_cost:
                    queue.append([i+1,j,tmp_cost,'v'])
                    min_dist[i+1][j] = tmp_cost
            if (0 <= i-1) and (board[i-1][j] == 0):
                tmp_cost = cost+600 if direc != 'v' else cost+100
                if min_dist[i-1][j] >= tmp_cost:
                    queue.append([i-1,j,tmp_cost, 'v'])
                    min_dist[i-1][j] = tmp_cost
            if (j+1 < length) and (board[i][j+1] == 0):
                tmp_cost = cost+600 if direc != 'h' else cost+100
                if min_dist[i][j+1] >= tmp_cost:
                    queue.append([i,j+1,tmp_cost,'h'])
                    min_dist[i][j+1] = tmp_cost
            if (j-1 >= 0) and (board[i][j-1] == 0):
                tmp_cost = cost+600 if direc != 'h' else cost+100
                if min_dist[i][j-1] >= tmp_cost:
                    queue.append([i,j-1,tmp_cost, 'h'])
                    min_dist[i][j-1] = tmp_cost
        return min_dist[-1][-1]
    return min(bfs(0,0,0,'h'), bfs(0,0,0,'v'))