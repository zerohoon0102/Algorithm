import sys
from collections import deque

value = sys.stdin.readline().rstrip()

i = 0
num = 0
result = 0
while(i < len(value)):
    if value[i] == "(":
        if value[i+1] == ")":
            result += num
            i += 1
        else:
            num += 1
            result += 1
    else:
        num -= 1
    i += 1
print(result)
