import sys
from collections import deque

N =int(sys.stdin.readline().rstrip())

arr = [0] + [1]*9

cnt = 1
while cnt < N:
    bef = -1
    cur = -1
    for i in range(10):
        if i == 0:
            cur = arr[i]
            arr[i] = arr[i+1]
        elif i == 9:
            bef = cur
            arr[i] = bef
        else:
            bef = cur
            cur = arr[i]
            arr[i] = bef + arr[i+1]
    cnt += 1

result = sum(arr)
print(result%1000000000)
