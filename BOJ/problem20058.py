import sys
from collections import deque
from copy import deepcopy

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, Q = map(int, input().rstrip().split())
value_dp = [2**n for n in range(N+1)]

table = [list(map(int, input().rstrip().split())) for _ in range(value_dp[N])]
L = list(map(int, input().rstrip().split()))

def rotate(y, x, length):
    global table
    for i in range(length//2):
        for j in range(length//2):
            cur = table[y+i][x+j]
            table[y+i][x+j] = table[y+length-1-j][x+i]
            table[y+length-1-j][x+i] = table[y+length-1-i][x+length-1-j]
            table[y+length-1-i][x+length-1-j] = table[y+j][x+length-1-i]
            table[y+j][x+length-i-1] = cur

def melt():
    global table
    stack = []
    for i in range(value_dp[N]):
        for j in range(value_dp[N]):
            if table[i][j] > 0:
                tmp = 0
                if i > 0:
                    if table[i-1][j] > 0:
                        tmp += 1
                if j < 2**N - 1:
                    if table[i][j+1] > 0:
                        tmp += 1
                if j > 0:
                    if table[i][j-1] > 0:
                        tmp += 1
                if i < 2**N - 1:
                    if table[i+1][j] > 0:
                        tmp += 1
                if tmp < 3:
                    stack.append((i,j))
    while stack:
        i,j = stack.pop()
        table[i][j] -= 1

for l in L:
    if l > 0:
        for i in range(0, value_dp[N], value_dp[l]):
            for j in range(0, value_dp[N], value_dp[l]):
                rotate(i, j, value_dp[l])
    melt()

value = [0,0]
queue = deque()
chk = [[True]*(value_dp[N]) for _ in range(value_dp[N])]

for i in range(value_dp[N]):
    for j in range(value_dp[N]):
        if not chk[i][j]:
            continue
        if table[i][j] <= 0:
            chk[i][j] = False
            continue
        queue.append((i,j))
        chk[i][j] = False
        max_ice = 0
        while queue:
            a, b = queue.popleft()
            value[0] += table[a][b]
            max_ice += 1
            if a > 0:
                if table[a-1][b] > 0 and chk[a-1][b]:
                    queue.append((a-1, b))
                    chk[a-1][b] = False
            if b > 0:
                if table[a][b-1] > 0 and chk[a][b-1]:
                    queue.append((a, b-1))
                    chk[a][b-1] = False
            if a < 2**N - 1:
                if table[a+1][b] > 0 and chk[a+1][b]:
                    queue.append((a+1, b))
                    chk[a+1][b] = False
            if b < 2**N - 1:
                if table[a][b+1] > 0 and chk[a][b+1]:
                    queue.append((a, b+1))
                    chk[a][b+1] = False
        
        value[1] = max(value[1], max_ice)
print(value[0])
print(value[1])
