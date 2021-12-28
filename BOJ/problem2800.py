import sys
from itertools import combinations

input_str = sys.stdin.readline().rstrip()

queue = []
pair = {}

for i, c in enumerate(input_str):
    if c == "(":
        queue.append(i)
    elif c == ")":
        pair[queue.pop()] = i

result = []
can = list(pair)
for i in range(1, len(can) + 1):
    perms = combinations(can, i)
    for perm in perms:
        tmp_str = list(input_str)
        for src in perm:
            tmp_str[src] = ""
            tmp_str[pair[src]] = ""
        result.append("".join(tmp_str))

for c in sorted(set(result)):
    print(c)


