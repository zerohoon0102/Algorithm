import sys
from collections import deque

def bfs():
    S = sys.stdin.readline().rstrip()
    queue = deque([(sys.stdin.readline().rstrip(), True)])

    while queue:
        T, direc = queue.popleft()
        if direc:
            if T[0] == 'B':
                if len(T) == len(S)+1:
                    if T[1:][::-1] == S:
                        return 1
                else:
                    queue.append((T[1:], not direc))
            if T[-1] == 'A':
                if len(T) == len(S) + 1:
                    if T[:-1] == S:
                        return 1
                else:
                    queue.append((T[:-1], direc))
        else:
            if T[-1] == 'B':
                if len(T) == len(S) + 1:
                    if T[:-1] == S:
                        return 1
                else:
                    queue.append((T[:-1], not direc))
            if T[0] == 'A':
                if len(T) == len(S) + 1:
                    if T[1:][::-1] == S:
                        return 1
                else:
                    queue.append((T[1:], direc))
    return 0

print(bfs())