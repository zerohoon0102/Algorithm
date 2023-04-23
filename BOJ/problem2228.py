import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

result = -100000000000
NULL = -3276801

# -------- DP --------
dp = [[NULL]*len(arr) for _ in range(M)]
for m in range(M):
    if m == 0:
        for i,v in enumerate(arr):
            if i == 0:
                dp[0][i] = v
            else:
                dp[0][i] = max(dp[0][i-1]+v, v)
    else:
        for i,v in enumerate(arr):
            if i < 2*m:
                continue
            
            if dp[m][i-1] != NULL:
                dp[m][i] = dp[m][i-1]+v
                
            dp[m][i] = max(dp[m][i], max(dp[m-1][:i-1])+v)
    print(dp[m])
result = max(dp[M-1])
print(result)
    
