def chk_all(t):
    n = len(t)
    for i in range(n):
        for j in range(n):
            if t[i][j][0] == 1:
                if i < n-1:
                    if t[i+1][j][0] == 0:
                        if (j == 0 and t[i][j][1] == 0) or (j == n-1 and t[i][j-1][1] == 0) or ((0 < j < n-1) and t[i][j][1] == 0 and t[i][j-1][1] == 0):
                            return False
            if t[i][j][1] == 1:
                if t[i+1][j][0] == 0 and t[i+1][j+1][0] == 0:
                    if (j == 0) or (j == n-2) or (t[i][j-1][1] == 0 or t[i][j+1][1] == 0):
                        return False
    return True

def solution(n, build_frame):
    t = [[[0,0] for _ in range(n+1)] for __ in range(n+1)]
    for frame in build_frame:
        x,y,a,b = frame
        if b == 1:
            if a == 0:
                t[n-y][x][0] = 1
                if y > 0:
                    if (t[n-y+1][x][0] == 0):
                        if x == 0:
                            if t[n-y][x][1] == 0:
                                t[n-y][x][0] = 0
                        elif x == n:
                            if t[n-y][x-1][1] == 0:
                                t[n-y][x][0] = 0
                        else:
                            if t[n-y][x][1] == 0 and t[n-y][x-1][1] == 0:
                                t[n-y][x][0] = 0
            elif a == 1:
                t[n-y][x][1] = 1
                if (t[n-(y-1)][x][0] == 0) and (t[n-y+1][x+1][0] == 0):
                    if x == 0 or x == n-1:
                        t[n-y][x][1] = 0
                    else:
                        if (t[n-y][x+1][1] == 0) or (t[n-y][x-1][1] == 0):
                            t[n-y][x][1] = 0
                    
        elif b == 0:
            if a == 0:
                t[n-y][x][0] = 0
                if not chk_all(t):
                    t[n-y][x][0] = 1
            elif a == 1:
                t[n-y][x][1] = 0
                if not chk_all(t):
                    t[n-y][x][1] = 1
    answer = []
    for i in range(n+1):
        for j in range(n+1):
            if t[i][j][0] == 1:
                answer.append([j,n-i, 0])
            if t[i][j][1] == 1:
                answer.append([j,n-i, 1])
    answer.sort()
    return answer