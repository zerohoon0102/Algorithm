from collections import defaultdict, deque
def solution(board):
    answer = 0
    N = len(board)
    
    block_info = defaultdict(dict)
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                block_num = board[i][j]
                block = block_info[block_num]
                if "cell" not in block:
                    block["cell"] = {}
                if j not in block["cell"]:
                    block["cell"][j] = []
                block["cell"][j].append(i)
    
    for key in block_info:
        block = block_info[key]
        keys = list(block["cell"])
        chk = True
        for idx in range(len(keys)-1):
            if max(block["cell"][keys[idx]]) != max(block["cell"][keys[idx+1]]):
                chk = False
                break
        if not chk:
            block["can"] = False
        else:
            block["can"] = True
            block["count"] = len(block["cell"])-1
            block["chk_top"] = False
    
    queue = deque([])
    for j in range(N):
        for i in range(N):
            if board[i][j] > 0:
                block = block_info[board[i][j]]
                if block["can"]:
                    if len(block["cell"][j]) == 1:
                        block["count"] -= 1
                        if block["count"] == 0:
                            queue.append(board[i][j])
                    else:
                        block["chk_top"] = True
                break
    
    while queue:
        answer += 1
        block_num = queue.popleft()
        block = block_info[block_num]
        for j in block["cell"]:
            for i in block["cell"][j]:
                board[i][j] = 0
            if len(block["cell"][j]) == 1 or block["chk_top"]:
                while i < N:
                    if board[i][j] > 0:
                        nxt_block = block_info[board[i][j]]
                        if nxt_block["can"]:
                            if len(nxt_block["cell"][j]) == 1:
                                nxt_block["count"] -= 1
                                if nxt_block["count"] == 0:
                                    queue.append(board[i][j])
                            else:
                                nxt_block["chk_top"] = True
                        break
                    i += 1
    
    return answer
