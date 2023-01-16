from collections import deque
def solution(info, edges):
    answer = 0
    tree = [[-1, -1] for _ in range(len(info))]
    for s,e in edges:
        if tree[s][0] == -1:
            tree[s][0] = e
        else:
            tree[s][1] = e
    
    answer = 0
    def dfs(can, ans, wolf_num):
        result = ans
        for c in can:
            if info[c] and ans <= wolf_num+1:
                continue
            nxt_can = can.copy()
            del nxt_can[c]
            for i in range(2):
                if tree[c][i] != -1:
                    nxt_can[tree[c][i]] = True
            if info[c]:
                result = max(result, dfs(nxt_can, ans, wolf_num+1))
            else:
                result = max(result, dfs(nxt_can, ans+1, wolf_num))
        return result
    answer = dfs({0: True}, 0, 0)
    
    return answer