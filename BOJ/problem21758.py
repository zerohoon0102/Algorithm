import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline
        
N = int(input())
arr = list(map(int, input().rstrip().split()))
total = sum(arr)
max_v = max(arr[1:N-1])

result = 0
# --- CASE 1 --- left 1 right 1
result = total - arr[0] - arr[-1] + max_v

# --- CASE 2 --- left 2 right 0
del_v = 0
i = 1
while i < N-1:
    result = max(result, total*2 - arr[0]*2 - arr[i]*2 - del_v)
    del_v += arr[i]
    i += 1
    
# --- CASE 3 --- left 0 right 2
del_v = 0
i = N-2
while i > 0:
    result = max(result, total*2 - arr[-1]*2 - arr[i]*2 - del_v)
    del_v += arr[i]
    i -= 1
print(result)