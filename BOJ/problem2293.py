import sys
from collections import deque
sys.setrecursionlimit(100000)

N, K = map(int, sys.stdin.readline().rstrip().split())

coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline().rstrip()))

count = [0]*(K+1)
count[0] = 1
for i in range(N):
    for j in range(coins[i], K+1):
        count[j] += count[j-coins[i]]

print(count[K])
