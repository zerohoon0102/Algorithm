import sys
from collections import deque, defaultdict
from heapq import heapify, heappush, heappop

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())
arr = []
info = defaultdict(int)

for _ in range(N):
    v = int(input())
    if v == 0:
        if len(arr) == 0:
            print(0)
        else:
            r = heappop(arr)
            if info[-r] > 0:
                print(-r)
                info[-r] -= 1
            else:
                print(r)
    else:
        heappush(arr, abs(v))
        if v < 0:
            info[v] += 1
