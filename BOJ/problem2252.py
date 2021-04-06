import sys

def double_arr(n, a):
    if a == None:
        return [[] for _ in range(n)]
    return [[a for _ in range(n)] for __ in range(n)]

N, M = map(int, sys.stdin.readline().split())

inDegree = [0]*(N+1)
line = double_arr(N+1, None)
queue = []

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    line[a].append(b)
    inDegree[b] += 1

for i in range(1, N+1):
    if inDegree[i] == 0:
        queue.append(i)

result = []
while(len(queue) > 0):
    num = queue.pop(0)
    for priority in line[num]:
        inDegree[priority] -= 1
        if inDegree[priority] == 0:
            queue.append(priority)
    result.append(str(num))

print(' '.join(result))