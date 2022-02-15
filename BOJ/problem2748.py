import sys

N = int(sys.stdin.readline().rstrip())

score = [0,1,1]
for i in range(3, N+1):
    score.append( score[i-1] + score[i-2] )

print(score[N])
