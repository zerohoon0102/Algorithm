from collections import deque

def dfs(node, idx, turns, turn, cycle):
    if node[idx]:
        for i, nxt_idx in enumerate(node[idx]):
            nxt_turn = turn + i*cycle
            dfs(node, nxt_idx, turns, nxt_turn, cycle*len(node[idx]))
    else:
        for i in range(turn, 10101, cycle):
            turns[i] = idx
                
    
def solution(edges, target):
    global leaf_node
    answer = []
    node = [[] for _ in range(len(edges)+1)]
    turns = [-1]*10101
    
    for parent, child in edges:
        node[parent-1].append(child-1)
    for i in range(len(node)):
        node[i].sort()
    
    dfs(node, 0, turns, 1, 1)
    
    chk = 0
    count_target = [[0, 0] for _ in range(len(target))]
    for i, v in enumerate(target):
        if v > 0:
            count_target[i][0] = v//3
            if v%3:
                count_target[i][0] += 1
            count_target[i][1] = v
            chk += 1
    
    cur = 1
    count = [0]*len(target)
    while 1:
        idx = turns[cur]
        
        count[idx] += 1
        if count[idx] == count_target[idx][0]:
            chk -= 1
            if chk == 0:
                break
        elif count[idx] > count_target[idx][1]:
            return [-1]
        cur += 1
    
    for i in range(1, cur+1):
        idx = turns[i]
        if target[idx]-1 <= 3*(count[idx]-1):
            answer.append(1)
            target[idx] -= 1
        elif target[idx]-2 <= 3*(count[idx]-1):
            answer.append(2)
            target[idx] -= 2
        else:
            answer.append(3)
            target[idx] -= 3
        count[idx] -= 1
    return answer
