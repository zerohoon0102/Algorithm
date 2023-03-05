import sys
from collections import deque, defaultdict
from heapq import heapify, heappush, heappop
from itertools import combinations

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())
month_day = {3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30,
             10: 31, 11: 30}
day_line = {3: 0}
for i in range(4, 12):
    day_line[i] = day_line[i-1] + month_day[i-1]

flowers = []
for _ in range(N):
    month_s, day_s, month_e, day_e = map(int, input().rstrip().split())
    if month_s == 12 or month_e < 3:
        continue
    if month_s < 3:
        month_s = 3
        day_s = 1
    if month_e == 12:
        month_e = 11
        day_e = 31
    
    start = day_line[month_s] + day_s
    end = day_line[month_e] + day_e - 1
    flowers.append((start, end))

flowers.sort(key = lambda x: (x[0], -x[1]))
if flowers[0][0] != 1:
    print(0)
else:
    start = 0
    end = 0
    result = 0

    max_end = 0
    for flower in flowers:
        s, e = flower
        if e <= end:
            continue
        if end < s-1:
            if max_end == 0:
                result = 0
                break
            end = max_end
            max_end = 0
            result += 1
        if end >= s-1:
            max_end = max(max_end, e)
    if max_end != 0 and end < day_line[11]+30:
        end = max_end
        result += 1
    if end != day_line[11]+30:
        result = 0
    print(result)
