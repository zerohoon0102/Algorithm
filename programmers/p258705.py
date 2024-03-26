def solution(n, tops):
    answer = 0
    merge_dp = [0]*(2*n + 1)
    alone_dp = [0]*(2*n + 1)
    
    merge_dp[0] = 1
    alone_dp[0] = 1
    
    merge_dp[1] = 2 if tops[0] else 1
    alone_dp[1] = 1
    for i in range(2, 2*n+1):
        if i%2 == 0:
            merge_dp[i] = alone_dp[i-1]
            alone_dp[i] = (merge_dp[i-1] + alone_dp[i-1])%10007
        else:
            merge_dp[i] = (2*alone_dp[i-1] + merge_dp[i-1])%10007 if tops[i//2] else alone_dp[i-1]
            alone_dp[i] = (merge_dp[i-1] + alone_dp[i-1])%10007
    
    return (alone_dp[-1] + merge_dp[-1])%10007
