import sys

C, M = list(map(int, sys.stdin.readline().rstrip().split()))
coin_arr = []

for _ in range(M):
    coin, client = list(map(int, sys.stdin.readline().rstrip().split()))
    coin_arr.append((client/coin, coin, client))

coin_arr.sort(key=lambda x: x[0])
dp = [200001]*(C+101)
dp[0] = 0

for _, coin, client in coin_arr:
    for i in range(client, C+101):
        if dp[i] > dp[i-client] + coin:
            dp[i] = dp[i-client] + coin

result = min(dp[C:])

print( result )
