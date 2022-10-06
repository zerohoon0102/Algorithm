import sys
from collections import deque, defaultdict

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, d, k, c = map(int, input().rstrip().split())
table = []
count = defaultdict(int)
queue = deque([])

cur = 1

for _ in range(N):
    table.append(int(input()))

count[c] += 1

for i in range(k):
    v = table[i]
    if count[v] == 0:
        cur += 1
    count[v] += 1
    queue.append(v)

result = cur
i = k
while i < N+k-1:
    b = queue.popleft()
    count[b] -= 1
    if count[b] == 0:
        cur -= 1
    
    v = table[i%N]
    queue.append(v)
    if count[v] == 0:
        cur += 1
        if cur > result:
            result = cur
    count[v] += 1
    i += 1

print(result)
