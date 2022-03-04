import sys
from itertools import combinations
from copy import deepcopy

N, M = list(map(int, sys.stdin.readline().rstrip().split()))
area = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

result = 0
zero = []
zero_num = 0
virus = []
for i in range(N):
    for j in range(M):
        if area[i][j] == 0:
            zero.append((i,j))
            zero_num += 1
        elif area[i][j] == 2:
            virus.append((i,j))

zero_num -= 3

def chk(arr):
    stack = deepcopy(virus)
    safe = zero_num
    while stack:
        i, j = stack.pop()
        if i > 0 and arr[i-1][j] == 0:
            arr[i-1][j] = 2
            safe -= 1
            stack.append((i-1,j))
        if i < N-1 and arr[i+1][j] == 0:
            arr[i+1][j] = 2
            safe -= 1
            stack.append((i+1,j))
        if j > 0 and arr[i][j-1] == 0:
            arr[i][j-1] = 2
            safe -= 1
            stack.append((i,j-1))
        if j < M-1 and arr[i][j+1] == 0:
            arr[i][j+1] = 2
            safe -= 1
            stack.append((i,j+1))
    
    return safe


for stone in combinations(zero, 3):
    new_area = deepcopy(area)
    for i,j in stone:
        new_area[i][j] = 1
    cur = chk(new_area)
    if cur > result:
        result = cur

print(result)
