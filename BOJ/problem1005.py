import sys
from collections import deque

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().rstrip().split())
    time = [0]
    time.extend(map(int, input().rstrip().split()))
    wait = [{} for _ in range(N+1)]
    pre = [[] for _ in range(N+1)]
    dp = time.copy()
    for _ in range(K):
        s, e = map(int, input().rstrip().split())
        wait[e][s] = True
        pre[s].append(e)
    W = int(input())
    
    queue = deque([])
    for i in range(1, N+1):
        if not wait[i]:
            queue.append(i)
    if not wait[W]:
        print(dp[W])
    while queue:
        c = queue.popleft()
        for nxt in pre[c]:
            dp[nxt] = max(dp[nxt], dp[c]+time[nxt])
            del wait[nxt][c]
            if not wait[nxt]:
                if nxt == W:
                    queue = deque([])
                    print(dp[W])
                    break
                queue.append(nxt)
