import sys
input = sys.stdin.readline

N, K, Q, M = map(int, input().rstrip().split())

arr_k = set(map(int, input().rstrip().split()))
arr_q = set(map(int, input().rstrip().split()))
arr = [1]*(N+3)

for q in sorted(arr_q - arr_k):
    if arr[q] == 0:
        continue
    val = 1
    while val*q < N+3:
        arr[val*q] = 0
        val += 1

for k in arr_k:
    arr[k] = 1

value = [0]*(N+3)
for i in range(3, N+3):
    value[i] = value[i-1] + arr[i]

for _ in range(M):
    S,E = map(int, input().rstrip().split())
    print(value[E] - value[S-1])
