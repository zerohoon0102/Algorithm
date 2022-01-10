import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().rstrip().split())

info = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    info[s].append(e)
    info[e].append(s)

for i in range(1, N+1):
    info[i] = sorted(set(info[i]))

# dfs
result = []
chk_table = [True for _ in range(N+1)]
chk_table[V] = False
def dfs(cur):
    result.append(str(cur))
    for nxt_v in info[cur]:
        if chk_table[nxt_v]:
            chk_table[nxt_v] = False
            dfs(nxt_v)
dfs(V)
print(' '.join(result))

# bfs
result.clear()
queue = deque([V])
chk_table = [True for _ in range(N+1)]
chk_table[V] = False
while(queue):
    v = queue.popleft()
    result.append(str(v))
    for nxt_v in info[v]:
        if chk_table[nxt_v]:
            queue.append(nxt_v)
            chk_table[nxt_v] = False

print(' '.join(result))

