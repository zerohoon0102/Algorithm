import sys

N = int(sys.stdin.readline().rstrip())

S = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [1]*N
result = 0

for i in range(N):
    for j in range(i):
        if S[j] < S[i] and dp[j]+1 > dp[i]:
            dp[i] = dp[j]+1
    if dp[i] > result:
        result = dp[i]

print(result)