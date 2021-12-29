import sys
from itertools import combinations


N = int(sys.stdin.readline().rstrip())

circle = []
for _ in range(N):
    x, r = map(int, sys.stdin.readline().rstrip().split())
    circle.append([x-r, x+r])

circle.sort(key=lambda x: (x[0], x[1]))

stack = []
chk = False
for i, src in enumerate(circle):
    if not stack:
        stack.append(src)
    else:
        while stack:
            if stack[-1][1] < src[0]:
                stack.pop()
            else:
                if stack[-1][0] == src[0] or src[0] <= stack[-1][1] <= src[1]:
                    chk = True
                break
        if chk:
            break
        stack.append(src)

if chk:
    print("NO")
else:
    print("YES")
