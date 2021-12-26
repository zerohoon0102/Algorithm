import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
cal = sys.stdin.readline().rstrip()
large = {}
operator = deque([])

for i in range(65, 65 + N):
    large[chr(i)] = sys.stdin.readline().rstrip()

for c in cal:
    if 65 <= ord(c) <= 90:
        operator.append(large[c])
    else:
        a = operator.pop()
        b = operator.pop()
        result = str(eval(b+c+a))
        operator.append(result)
        #operator.append(c)

print(f"{float(operator[0]):0.2f}")
