import sys
sys.setrecursionlimit(1000000)
from collections import deque

input = sys.stdin.readline    

N = int(input().rstrip())
lines = set()
for _ in range(N):
    lines.add(input().rstrip())
info = {}

for line in lines:
    p, _, q = line.split()
    if p in info:
        info[p].add(q)
    else:
        info[p] = set([q])

result = ""
n = 0
for _ in range(len(info)):
    for k in info:
        tmp = list(info[k])
        for n_x in tmp:
            if n_x in info:
                info[k].update(info[n_x])
for p in sorted(info):
    for q in sorted(info[p]):
        if p == q:
            continue
        result += f"{p} => {q}\n"
        n += 1
print(n)
print(result.rstrip())
