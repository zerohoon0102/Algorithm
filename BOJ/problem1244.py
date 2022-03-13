import sys

N = int(sys.stdin.readline().rstrip())

board = list(map(int, sys.stdin.readline().rstrip().split()))

S = int(sys.stdin.readline().rstrip())
for _ in range(S):
    gender, num = map(int, sys.stdin.readline().rstrip().split())
    if gender == 1:
        cur = num
        while cur <= N:
            board[cur-1] = abs(board[cur-1]-1)
            cur += num
    else:
        count = 1
        board[num-1] = abs(board[num-1]-1)
        while num-count > 0 and num+count <= N and board[num-count-1] == board[num+count-1]:
            board[num-count-1] = abs(board[num-count-1]-1)
            board[num+count-1] = board[num-count-1]
            count += 1

result = ""
for i in range(N):
    result += str(board[i]) + " "
    if i%20 == 19 and i < N-1:
        print(result.rstrip())
        result = ""
print(result.rstrip())
