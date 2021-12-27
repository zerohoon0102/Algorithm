import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
linked_list = []

for i, num in enumerate(map(int, sys.stdin.readline().rstrip().split())):
    linked_list.append([i-1, num, i+1])
linked_list[0][0] = n-1
linked_list[n-1][2] = 0

i = 0
result = []
for _ in range(n):
    bef, num, aft = linked_list[i]
    result.append(str(i+1))
    linked_list[bef][2] = aft
    linked_list[aft][0] = bef
    if num > 0:
        for __ in range(num):
            i = linked_list[i][2]
    else:
        for __ in range(-num):
            i = linked_list[i][0]

print(' '.join(result))
