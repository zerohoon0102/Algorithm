import sys
sys.setrecursionlimit(5000)

N, K = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
chk_list = [True]*(N+1)
result = False

stack = [0]
while(stack):
    i = stack.pop()
    j = i + 1
    while( j < len(A) ):
        if chk_list[j]:
            if (abs(A[i] - A[j]) + 1)*(j-i) <= K:
                if j == len(A) - 1:
                    result = True
                    stack.clear()
                    break
                elif j < len(A) - 1:
                    stack.append(j)
                    chk_list[j] = False
        j += 1

if result:
    print('YES')
else:
    print('NO')
