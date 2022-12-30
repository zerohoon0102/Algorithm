import sys
from collections import deque

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

r1, c1, r2, c2 = map(int, input().rstrip().split())

result = [[-1]*(c2-c1+1) for _ in range(r2-r1+1)]

queue = deque([(r1, c1, 0, 0)])

while queue:
    r, c, i, j = queue.popleft()
    a_r, a_c = abs(r), abs(c)
    
    if a_r >= a_c:
        n = a_r
    else:
        n = a_c

    v = 1 + 4*n
    if n > 1:
        n_t = n-1
        v += 8*int((n_t*(n_t+1))/2)
    
    cur_r, cur_c = -abs(n), -abs(n)
    if c == -n:
        v += r - (-n)
    elif r == n:
        v += 2*r
        v += c - (-n)
    elif c == n:
        v -= 2*c
        v -= r - (-n)
    elif r == -n:
        v -= c - (-n)
    result[i][j] = v
    
    if r < r2 and result[i+1][j] == -1:
        result[i+1][j] = 0
        queue.append((r+1, c, i+1, j))
    if c < c2 and result[i][j+1] == -1:
        result[i][j+1] = 0
        queue.append((r, c+1, i, j+1))

result_str = []
for arr in result:
    a = list(map(str, arr))
    result_str.append(a)

max_length = 0
for j in range(c2-c1+1):
    for i in range(r2-r1+1):
        max_length = max(max_length, len(result_str[i][j]))

for j in range(c2-c1+1):
    for i in range(r2-r1+1):
        result_str[i][j] = ' '*(max_length-len(result_str[i][j])) + result_str[i][j]

for arr in result_str:
    print(' '.join(arr))
