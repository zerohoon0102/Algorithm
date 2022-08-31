import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().rstrip().split())

roads = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().rstrip().split())
    roads[s].append(e)

result = [300001]*(N+1)
result[X] = 0

queue = deque([X])
while queue:
    cur = queue.popleft()
    for nxt in roads[cur]:
        if result[cur] + 1 < result[nxt] and result[cur]+1 <= K:
            result[nxt] = result[cur] + 1
            queue.append(nxt)

chk = True
for i,v in enumerate(result):
    if v == K:
        print(i)
        chk = False
if chk:
    print(-1)
