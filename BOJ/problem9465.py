import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(2)]

    dp = [[0,0] for _ in range(N)]
    dp[0][0] = board[0][0]
    dp[0][1] = board[1][0]
    if N > 1:
        dp[1][0] = board[1][0] + board[0][1]
        dp[1][1] = board[0][0] + board[1][1]

        for n in range(2, N):
            dp[n][0] = max(dp[n-2][1], dp[n-1][1]) + board[0][n]
            dp[n][1] = max(dp[n-2][0], dp[n-1][0]) + board[1][n]
        print(max(max(dp[-1]), max(dp[-2])))
    else:
        print(max(dp[0]))
