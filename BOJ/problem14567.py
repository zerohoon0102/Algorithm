import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

chk = [0]*(N+1)
before = [0]*(N+1)
after = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().rstrip().split())
    before[B] += 1
    after[A].append(B)

n = 0
cur = 1
while n < N:
    hear = []
    for i in range(1, N+1):
        if chk[i]:
            continue
        
        if before[i] == 0:
            chk[i] = str(cur)
            hear.append(i)
            n += 1
    for h in hear:
        for aft in after[h]:
            before[aft] -= 1
    cur += 1

print(' '.join(chk[1:]))
