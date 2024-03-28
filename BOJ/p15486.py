import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*(N+1)

max_p = 0
for idx in range(1, N+1):
    t, p = map(int, input().split())
    max_p = max(max_p, dp[idx-1])
    if idx+t-1 <= N:
        dp[idx+t-1] = max(dp[idx+t-1], max_p + p)
print(max(max_p, dp[N]))
