import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline    

N, M = map(int,input().rstrip().split())
arr = [i for i in range(N+1)]

def find(cur):
    if arr[cur] != cur:
        arr[cur] = find(arr[cur])
    return arr[cur]

for _ in range(M):
    t, a, b = map(int, input().rstrip().split())
    if t == 0:
        if a == b:
            continue
        parent_a, parent_b = find(a), find(b)
        if parent_a == parent_b:
            continue
        arr[parent_a] = parent_b
    elif t == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
