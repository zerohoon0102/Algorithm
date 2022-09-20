import sys

input = sys.stdin.readline    

D, P = map(int, input().rstrip().split())
arr = [tuple(map(int, input().rstrip().split())) for _ in range(P)]
dp = [-1]*(D+1)
dp[0] = 2**31

for l, c in arr:
    for i in range(D, l-1, -1):
        if dp[i-l] == -1:
            continue
        dp[i] = max(dp[i], min(dp[i-l],c))
print(dp[-1])
