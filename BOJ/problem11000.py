import sys
from collections import deque, defaultdict

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())
info = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
value = defaultdict(int)
result = 0
for s, t in info:
    value[s] += 1
    value[t] -= 1

cur = 0
for v in sorted(value):
    cur += value[v]
    result = max(result, cur)

print(result)
