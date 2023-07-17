import sys
from collections import defaultdict
from itertools import combinations
import math

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().rstrip().split()))
count = [defaultdict(int), 0, defaultdict(int)]
count_two = [defaultdict(int), 0, defaultdict(int)]

for v in arr:
    if v < 0:
        count[0][v] += 1
    elif v == 0:
        count[1] += 1
    else:
        count[2][v] += 1

for i in (0, 2):
    for key1, key2 in combinations(count[i], 2):
        v1, v2 = count[i][key1], count[i][key2]
        count_two[i][key1+key2] += v1*v2
    for key in count[i]:
        v1 = count[i][key]
        count_two[i][key*2] += math.comb(v1, 2)

result = 0
for key in count[0]:
    tmp = count[0][key]*count[1]*count[2][-key]
    tmp += count[0][key]*count_two[2][-key]
    result += tmp

for key in count_two[0]:
    tmp = count_two[0][key]*count[2][-key]
    result += tmp
result += math.comb(count[1], 3)
print(result)
