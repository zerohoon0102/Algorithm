import sys
from collections import Counter

N = int(sys.stdin.readline())

for _ in range(N):
    value = sys.stdin.readline()
    count = Counter(value)
    if count['('] != count[')']:
        print("NO")
        continue
    left = 0
    right = 0
    for i in range(len(value)):
        if value[i] == "(":
            left += 1
        elif value[i] == ")":
            right += 1
        if right > left:
            print("NO")
            break
        if i == len(value) - 1:
            print("YES")
