import sys
from collections import deque

input = sys.stdin.readline    

N = int(input().rstrip())
table = [tuple(map(int, input().rstrip().split())) for _ in range(N)]

def check(y, x, n):
    sum_board = 0
    for i in range(y, y+n):
        sum_board += sum(table[i][x:x + n])
    if sum_board == 0:
        return 1
    if sum_board == n**2:
        return 0
    return 2

white, blue = 0, 0
queue = deque([(0, 0, N)])
while queue:
    cur_y, cur_x, width = queue.popleft()
    val = check(cur_y, cur_x, width)
    if val == 1:
        white += 1
    elif val == 0:
        blue += 1
    else:
        queue.append((cur_y, cur_x, width//2))
        queue.append((cur_y + width//2, cur_x, width//2))
        queue.append((cur_y, cur_x + width//2, width//2))
        queue.append((cur_y + width//2, cur_x + width//2, width//2))

print(white)
print(blue)
