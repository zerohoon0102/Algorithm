import sys
from itertools import accumulate

N, M = map(int, sys.stdin.readline().rstrip().split())

table = [list(accumulate(map(int, sys.stdin.readline().rstrip().split()))) for _ in range(N)]

# O(N^2)
for i in range(N):
    for j in range(N-1):
        table[j+1][i] += table[j][i]

# O(M)
for _ in range(M):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().rstrip().split())

    if x1 > 1 and y1 > 1:
        result = table[y2-1][x2-1] - table[y2-1][x1-2] - table[y1-2][x2-1] + table[y1-2][x1-2]
    elif x1 > 1 and y1 == 1:
        result = table[y2-1][x2-1] - table[y2-1][x1-2]
    elif x1 == 1 and y1 > 1:
        result = table[y2-1][x2-1] - table[y1-2][x2-1]
    else:
        result = table[y2-1][x2-1]
    print(result)

# 시간 복잡도는 O(3*N^2) + O(M) => O(N^2 + M)이다
# 이때 N은 1024이하이고, M은 100,000 이하이므로, 약 O(100000) 으로 볼 수 있다.
