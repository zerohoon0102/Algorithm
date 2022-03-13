import sys

N = int(sys.stdin.readline().rstrip())

road = list(map(int, sys.stdin.readline().rstrip().split()))
cost = list(map(int, sys.stdin.readline().rstrip().split()))

cur = 0
low = 1000000001
result = 0

for i in range(N-1):
    cur = cost[i]
    if cur < low:
        low = cur
    result += road[i]*low
print(result)
