import sys
from collections import deque
import heapq

input = sys.stdin.readline    

T = int(input().rstrip())
for _ in range(T):
    k = int(input().rstrip())
    min_heap = []
    max_heap = []
    Q = {}
    
    for __ in range(k):
        cmd, n = input().rstrip().split()
        n = int(n)
        if cmd == 'I':
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
            if n in Q:
                Q[n] += 1
            else:
                Q[n] = 1
        else:
            if n == 1 and Q:
                while 1:
                    v = -heapq.heappop(max_heap)
                    if v in Q:
                        if Q[v] == 1:
                            del Q[v]
                        else:
                            Q[v] -= 1
                        break
            elif n == -1 and Q:
                while 1:
                    v = heapq.heappop(min_heap)
                    if v in Q:
                        if Q[v] == 1:
                            del Q[v]
                        else:
                            Q[v] -= 1
                        break
                
    if not Q:
        print("EMPTY")
    else:
        while 1:
            max_v = -heapq.heappop(max_heap)
            if max_v in Q:
                break
        while 1:
            min_v = heapq.heappop(min_heap)
            if min_v in Q:
                break
        print(max_v, min_v)
