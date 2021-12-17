import sys
from collections import Counter, deque

N = int(sys.stdin.readline().rstrip())

queue = deque([])
for _ in range(N):
    value = sys.stdin.readline().rstrip()
    if value == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif value == "size":
        print(len(queue))
    elif value == "empty":
        print(int(len(queue) == 0))
    elif value == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif value == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    else:
        num = int(value[5:])
        queue.append(num)
