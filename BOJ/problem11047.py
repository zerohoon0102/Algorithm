import sys

N, k = map(int, sys.stdin.readline().split())

arr = [int(sys.stdin.readline()) for _ in range(N)]

result = 0
for i in range(N-1, -1, -1):
    div = k//arr[i]
    k -= div*arr[i]
    result += div
    print(f"i : {i}, result: {result}")

print(result)
