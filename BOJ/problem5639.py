import sys
from collections import deque

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

class Node:
    def __init__(self, value):
        self.value = value
        self.max = 10**6
        self.min = 0
        
        self.left = None
        self.right = None
        self.parent = None

root = None
arr = deque([])
bef_v = 0
while 1:
    v = input().rstrip()
    if v == "":
        break
    v = int(v)
    arr.append(Node(v))

root = arr.popleft()
bef = root
while arr:
    node = arr.popleft()
    while 1:
        if bef.value > node.value and bef.min < node.value:
            if bef.left == None:
                bef.left = node
                node.parent = bef
                node.min = bef.min
                node.max = bef.value
                bef = node
                break
            else:
                bef = bef.left
                continue
        if bef.value < node.value and bef.max > node.value:
            if bef.right == None:
                bef.right = node
                node.parent = bef
                node.min = bef.value
                node.max = bef.max
                bef = node
                break
            else:
                bef = bef.right
                continue
        bef = bef.parent

def dfs(node):
    cur = node
    if node.left != None:
        dfs(node.left)
    if node.right != None:
        dfs(node.right)
    print(cur.value)

dfs(root)