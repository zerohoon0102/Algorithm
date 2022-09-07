import sys
from itertools import combinations

input = sys.stdin.readline    

N = int(input().rstrip())
table = [list(map(int, input().rstrip().split())) for _ in range(N)]
tmp = []
for i in range(1, N-1):
    for j in range(1, N-1):
        tmp.append((i,j))
comb = list(combinations(tmp,3))
result = 2000000000
for src in comb:
    if (((src[0][0]-src[1][0])**2 + (src[0][1]-src[1][1])**2) <= 4 or
        ((src[0][0]-src[2][0])**2 + (src[0][1]-src[2][1])**2) <= 4 or
        ((src[1][0]-src[2][0])**2 + (src[1][1]-src[2][1])**2) <= 4):
        continue
    total = 0
    for y,x in src:
        total += table[y-1][x] + sum(table[y][x-1:x+2]) + table[y+1][x]
    if total < result:
        result = total
print(result)
