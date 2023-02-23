import sys
from collections import deque, defaultdict
from heapq import heapify, heappush, heappop
from itertools import combinations

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

N = int(input())
nodes = [None]*(N+1)
w = 1
h = 1
height_min = [10001]*10001
height_max = [0]*10001
chk_root = [True]*(N+1)

for _ in range(N):
    i, left, right = map(int, input().rstrip().split())
    node = Node(i, left, right)
    if left > 0:
        chk_root[left] = False
    if right > 0:
        chk_root[right] = False
    nodes[i] = node

def dfs(idx, level):
    global w
    node = nodes[idx]
    if node.left != -1:
        dfs(node.left, level+1)
    if height_min[level] > w:
        height_min[level] = w
    if height_max[level] < w:
        height_max[level] = w
    w += 1
    if node.right != -1:
        dfs(node.right, level+1)
root = 1
for i in range(1, N+1):
    if chk_root[i]:
        root = i
        break

dfs(root, 1)
result = [-1, -1]
for i in range(1, 10001):
    if height_max[i] == 0:
        break
    value = height_max[i]-height_min[i]
    if value > result[1]:
        result[0] = i
        result[1] = value
print(result[0], result[1]+1)
