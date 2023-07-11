import sys
from collections import deque
import heapq

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
board = [tuple(map(abs, map(int, input().rstrip().split()))) for _ in range(N)]

if M > 1:
    arr = [[0]*N for _ in range(N)]
    horizontal = [[0]*N for _ in range(N)]
    vertical = [[0]*N for _ in range(N)]

    h_M = M//2
    for i in range(h_M, N-h_M):
        for j in range(h_M, N-h_M):
            c_i, c_j = i-h_M, j-h_M
            
            # horizontal sum
            h_v = horizontal[i][j-1] - arr[i][max(0, j-M)]
            
            # vertical sum
            v_v = vertical[i-1][j]
            
            # result
            v = board[c_i][c_j] - h_v - v_v
            arr[i][j] = v
            horizontal[i][j] = h_v + v
            vertical[i][j] = v_v + horizontal[i][j] - horizontal[max(0, i-M+1)][j]

    for tmp in arr:
        print(' '.join(map(str,tmp)))
else:
    for tmp in board:
        print(' '.join(map(str,tmp)))
