import sys
from collections import deque

input = sys.stdin.readline    

N, L, R = map(int, input().rstrip().split())

table = [list(map(int, input().rstrip().split())) for _ in range(N)]
result = 0
mt = [[True]*N for _ in range(N)]
while 1:
    tmp = [0]
    chk = [[True]*N for _ in range(N)]
    queue = deque([])
    not_nxt = True
    for i in range(N):
        for j in range(N):
            if not chk[i][j] or not mt[i][j]:
                continue
            chk[i][j] = False
            queue.append((i, j))
            while queue:
                y, x = queue.popleft()
                tmp[0] += table[y][x]
                tmp.append((y,x))
                if y > 0 :
                    if (L <= abs(table[y][x] - table[y-1][x]) <= R) and chk[y-1][x] and (mt[y-1][x] or mt[y][x]):
                        queue.append((y-1,x))
                        chk[y-1][x] = False
                if y < N-1 :
                    if (L <= abs(table[y][x] - table[y+1][x]) <= R) and chk[y+1][x] and (mt[y][x] or mt[y+1][x]):
                        queue.append((y+1,x))
                        chk[y+1][x] = False
                if x > 0:
                    if (L <= abs(table[y][x] - table[y][x-1]) <= R) and chk[y][x-1] and (mt[y][x] or mt[y][x-1]):
                        queue.append((y,x-1))
                        chk[y][x-1] = False
                if x < N-1:
                    if (L <= abs(table[y][x] - table[y][x+1]) <= R) and chk[y][x+1] and (mt[y][x] or mt[y][x+1]):
                        queue.append((y,x+1))
                        chk[y][x+1] = False
                mt[y][x] = False
            if len(tmp) > 2:
                val = tmp[0]//(len(tmp)-1)
                not_nxt = False
                for idx in range(1, len(tmp)):
                    y,x = tmp[idx]
                    table[y][x] = val
                    mt[y][x] = True
            tmp = [0]
    if not_nxt:
        break
    result += 1
print(result)
