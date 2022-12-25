import sys
from heapq import heapify, heappush, heappop

input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    M = int(input())
    print(M//2 + 1)
    arr = []
    for _ in range(M//10 + 1):
        arr.extend(list(map(int, input().rstrip().split())))
    cur = arr[0]
    less = []
    more = []
    result = [str(cur)]
    for i in range(1, M):
        if arr[i] < cur:
            heappush(less, -arr[i])
            while len(less) > len(more):
                heappush(more, cur)
                cur = -heappop(less)
        else:
            heappush(more, arr[i])
            while len(more) > len(less):
                heappush(less, -cur)
                cur = heappop(more)
        if i%2 == 0:
            result.append(str(cur))
            if len(result)%10 == 0:
                print(' '.join(result))
                result = []
    print(' '.join(result))
