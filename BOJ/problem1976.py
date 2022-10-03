import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

route = [[] for _ in range(N)]
for i in range(N):
    a = tuple(map(int, input().rstrip().split()))
    for j,v in enumerate(a):
        if j > i:
            if v:
                route[i].append(j)

uaf = [i for i in range(N)]
def find_root(cur):
    if uaf[cur] != cur:
        uaf[cur] = find_root(uaf[cur])
    return uaf[cur]

result = 'YES'

for i, dests in enumerate(route):
    for dest in dests:
        if find_root(dest) < find_root(i):
            uaf[uaf[i]] = uaf[dest]
        else:
            uaf[uaf[dest]] = uaf[i]

for i in range(N):
    find_root(i)

visit = list(map(int, input().rstrip().split()))
for i in range(len(visit)-1):
    if uaf[visit[i+1]-1] != uaf[visit[i]-1]:
        result = 'NO'
        break
print(result)
