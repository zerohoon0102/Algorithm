import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

computer = [True for i in range(N+1)]
edge = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edge[a].append(b)
    edge[b].append(a)

queue = deque([1])
cnt = 0
computer[1] = False

while(queue):
    i = queue.popleft()
    for j in edge[i]:
        if computer[j]:
            computer[j] = False
            queue.append(j)
            cnt += 1

print(cnt)
