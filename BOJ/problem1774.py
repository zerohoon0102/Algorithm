import sys
from itertools import combinations
import math

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def find(i):
    p = parent[i]
    if p != i:
        parent[i] = find(p)
    return parent[i]

N, M = map(int, input().rstrip().split())
gods = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
parent = [i for i in range(N)]
distance = [[0]*N for _ in range(N)]

for A in range(N):
    for B in range(A+1, N):
        d = math.sqrt((gods[A][0]-gods[B][0])**2 + (gods[A][1]-gods[B][1])**2)
        distance[A][B] = d
        distance[B][A] = d

candidates = sorted(combinations(range(N), 2), key=lambda x: -distance[x[0]][x[1]])
result = 0

for _ in range(M):
    A, B = map(int, input().rstrip().split())
    A -= 1
    B -= 1
    parent_A, parent_B = find(A), find(B)
    if parent_A < parent_B:
        parent[parent_B] = parent_A
    elif parent_A > parent_B:
        parent[parent_A] = parent_B

while candidates:
    A, B = candidates.pop()
    parent_A, parent_B = find(A), find(B)
    if parent_A == parent_B :
        continue
    result += distance[A][B]
    
    if parent_A < parent_B:
        parent[parent_A] = parent_B
    else:
        parent[parent_B] = parent_A

print(format(round(result, 2), ".2f"))
