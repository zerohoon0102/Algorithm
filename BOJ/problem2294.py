import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())

coins = []

chk = [True]*(k+1)

for _ in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))

queue = deque([(coin, 1) for coin in coins])

while queue:
    for _ in range(len(queue)):
        score, num = queue.popleft()
        if score == k:
            print(num)
            exit()
        else:
            for coin in coins:
                nxt_score = score + coin
                if nxt_score <= k and chk[nxt_score]:
                    queue.append((nxt_score, num+1))
                    chk[nxt_score] = False

print(-1)
