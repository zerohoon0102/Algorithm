import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

def bfs():
    if N >= K:
        return N-K
    else:
        chk = [100000]*(100002)
        chk[N] = 0
        queue = deque([N])
        while queue:
            n = queue.popleft()
            if 2*n <= K+1 and chk[2*n] == 100000:
                chk[2*n] = chk[n]
                if 2*n == K:
                    return chk[K]
                queue.append(2*n)
            if n-1 >= 0 and chk[n-1] == 100000:
                chk[n-1] = chk[n] + 1
                if n-1 == K:
                    return chk[K]
                queue.append(n-1)
            if n+1 <= K+1 and chk[n+1] == 100000:
                chk[n+1] = chk[n] + 1
                if n+1 == K:
                    return chk[K]
                queue.append(n+1)

print( bfs() )
