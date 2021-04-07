import sys

N = int(sys.stdin.readline())

inDegree = [0]*(N+1)
line = [[] for _ in range(N+1)]
queue = []
time = [0]*(N+1)
result = [0]*(N+1)

for i in range(1, N+1):
    tmp_info = list(map(int, sys.stdin.readline().split()))
    tmp_info.remove(-1)
    tmp_time = tmp_info.pop(0)
    time[i] = tmp_time
    result[i] = tmp_time
    for bef in tmp_info:
        line[bef].append(i)
        inDegree[i] += 1

    
for i in range(1, N+1):
    if inDegree[i] == 0:
        queue.append(i)

try_num = 0
while(len(queue) > 0):
    num = queue.pop(0)
    for idx in line[num]:
        result[idx] = max(result[idx], result[num] + time[idx])
        inDegree[idx] -= 1
        if inDegree[idx] == 0:
            queue.append(idx)

for i in range(1, N+1):
    print(result[i])