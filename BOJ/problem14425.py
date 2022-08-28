import sys

N, M = map(int, sys.stdin.readline().split())

arr = {sys.stdin.readline().rstrip(): '' for _ in range(N)}

result = 0
for _ in range(M):
    if sys.stdin.readline().rstrip() in arr:
        result += 1
print(result)

