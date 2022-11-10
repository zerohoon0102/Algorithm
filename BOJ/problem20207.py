import sys
from collections import deque
from copy import deepcopy

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())
sched = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
days = [0]*366

for s,e in sched:
    for i in range(s, e+1):
        days[i] += 1
result = 0
tmp_max = 0
length = 0
for i in range(1, 366):
    v = days[i]
    if v == 0:
        if tmp_max > 0:
            result += tmp_max*length
            length = 0
            tmp_max = 0
        continue
    length += 1
    tmp_max = max(tmp_max, v)
result += tmp_max*length
print(result)
