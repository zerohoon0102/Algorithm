import sys
sys.setrecursionlimit(1000000)
from collections import deque

input = sys.stdin.readline    

H, W = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
table = [[1]*W for _ in range(H)]
for i, v in enumerate(arr):
    for j in range(v):
        table[H-j-1][i] = 0

v = arr[0]
i = 0
while i < W:
    if arr[i] == H:
        break
    if arr[i] > v:
        v = arr[i]
    for a in range(H-v):
        table[a][i] = 0
    i += 1

v = arr[-1]
i = W-1
while i >= 0:
    if arr[i] == H:
        break
    if arr[i] > v:
        v = arr[i]
    for a in range(H-v):
        table[a][i] = 0
    i -= 1

result = 0
for a in table:
    result += sum(a)
print(result)
