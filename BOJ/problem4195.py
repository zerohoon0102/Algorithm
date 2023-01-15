import sys
from collections import deque, defaultdict
from heapq import heapify, heappush, heappop
from itertools import combinations

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def union(name_num, parent):
    if parent[name_num] != name_num:
        parent[name_num] = union(parent[name_num], parent)
    return parent[name_num]

N = int(input())
for _ in range(N):
    count = 0
    F = int(input())
    name_to_num = {}
    parent = []
    value = []
    for _ in range(F):
        a, b = input().rstrip().split()
        if a not in name_to_num:
            name_to_num[a] = count
            parent.append(count)
            value.append(1)
            count += 1
        if b not in name_to_num:
            name_to_num[b] = count
            parent.append(count)
            value.append(1)
            count += 1
        
        a_i, b_i = name_to_num[a], name_to_num[b]
        p_a = union(a_i, parent)
        p_b = union(b_i, parent)
        if p_a < p_b:
            parent[p_b] = p_a
            value[p_a] += value[p_b]
        elif p_a > p_b:
            parent[p_a] = p_b
            value[p_b] += value[p_a]
        print(value[union(a_i, parent)])
