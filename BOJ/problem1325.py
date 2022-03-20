import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
trust = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())

    trust[B].append(A)

def bfs(i):
    chk = [True]*(N+1)
    queue = deque([i])
    count = 1
    chk[i] = False
    while queue:
        cur = queue.popleft()
        for j in trust[cur]:
            if chk[j]:
                chk[j] = False
                count += 1
                queue.append(j)
    return count

result = ""
mx = 0
for i in range(1, N+1):
    count = bfs(i)
    print(count)
    if count == mx:
        result += f"{i} "
    elif count > mx:
        result = f"{i} "
        mx = count

print(result.rstrip())
