import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    priority = {i:0 for i in range(1, 10)}
    num_arr = deque([])
    max_num = 0
    for i, num in enumerate(map(int, sys.stdin.readline().rstrip().split())):
        num_arr.append([i,num])
        priority[num] += 1
        if num > max_num:
            max_num = num
    cnt = 0
    while(1):
        idx, num = num_arr.popleft()
        if num < max_num:
            num_arr.append([idx, num])
        else:
            cnt += 1
            if idx == M:
                print(cnt)
                break
            priority[num] -= 1
            while priority[num] == 0:
                num -= 1
            max_num = num
