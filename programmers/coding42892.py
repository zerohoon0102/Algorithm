from collections import deque
import sys
sys.setrecursionlimit(10**6)
bef = list()
aft = list()

def build_tree(info, idx, tree, level, left, right):
    node = tree[idx]
    chk_level_idx = level.index(node[1])
    if chk_level_idx < len(level) - 1:
        chk_level_idx += 1
        for tmp_node in info[level[chk_level_idx]]:
            if idx%2 == 0:
                if (tmp_node[0] < node[0]) and (tmp_node[0] > left):
                    tree[2*idx] = tmp_node
                    build_tree(info, 2*idx, tree, level, left,node[0])
                elif (tmp_node[0] > node[0]) and (tmp_node[0] < right):
                    tree[2*idx + 1] = tmp_node
                    build_tree(info, 2*idx+1, tree, level, node[0], right)
            elif idx%2 == 1:
                if (tmp_node[0] < node[0]) and (tmp_node[0] > left):
                    tree[2*idx] = tmp_node
                    build_tree(info, 2*idx, tree, level, left,node[0])
                elif (tmp_node[0] > node[0]) and (tmp_node[0] < right):
                    tree[2*idx + 1] = tmp_node
                    build_tree(info, 2*idx+1, tree, level, node[0], right)

def bef_tree(tree, idx, arr):
    arr.append(tree[idx][2])
    if 2*idx in tree:
        bef_tree(tree,2*idx,arr)
    if (2*idx + 1) in tree:
        bef_tree(tree, 2*idx + 1, arr)
def aft_tree(tree, idx, arr):
    if 2*idx in tree:
        aft_tree(tree,2*idx,arr)
    if (2*idx + 1) in tree:
        aft_tree(tree, 2*idx + 1, arr)
    arr.append(tree[idx][2])
def solution(nodeinfo):
    info = {}
    for idx in range(len(nodeinfo)):
        if nodeinfo[idx][1] not in info:
            info[nodeinfo[idx][1]] = [[nodeinfo[idx][0], nodeinfo[idx][1], idx+1]]
        else:
            info[nodeinfo[idx][1]].append([nodeinfo[idx][0], nodeinfo[idx][1], idx+1])
    level = sorted(info, reverse=True)
    tree = {1:info[level[0]][0]}
    build_tree(info, 1, tree, level, -1, 100001)
    bef_tree(tree, 1, bef)
    aft_tree(tree, 1, aft)
    answer = [bef,aft]
    return answer