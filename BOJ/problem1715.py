from heapq import heapify, heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    heappush(arr, int(input()))

answer = 0
while len(arr) > 1:
    n, m = heappop(arr), heappop(arr)
    nxt = n+m
    answer += nxt
    heappush(arr, nxt)
print(answer)
