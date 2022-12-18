from collections import deque

def solution(alp, cop, problems):
    problems.append([0,0,0,1,1])
    problems.append([0,0,1,0,1])
    alp_problems = sorted(problems, key=lambda x: (-(x[2]/x[4]), x[4]))
    cop_problems = sorted(problems, key=lambda x: (-(x[3]/x[4]), x[4]))
    
    target = [alp,cop]
    for problem in problems:
        target[0] = max(target[0], problem[0])
        target[1] = max(target[1], problem[1])
    dp = [[100000000]*(target[1]+1) for _ in range(target[0]+1)]
    dp[alp][cop] = 0
    
    queue = deque([(alp,cop)])
    while queue:
        alp, cop = queue.popleft()
        cost = dp[alp][cop]
        if alp >= target[0] and cop >= target[1]:
            continue
        elif alp < target[0] and cop < target[1]:
            for problem in problems:
                if alp >= problem[0] and cop >= problem[1] :
                    nxt_cost = cost+problem[4]
                    nxt_alp = alp+problem[2]
                    nxt_cop = cop+problem[3]
                    
                    nxt_alp = min(nxt_alp, target[0])
                    nxt_cop = min(nxt_cop, target[1])
                    
                    if dp[nxt_alp][nxt_cop] > nxt_cost:
                        dp[nxt_alp][nxt_cop] = nxt_cost
                        queue.append((nxt_alp, nxt_cop))
        elif alp < target[0] and cop >= target[1]:
            for problem in alp_problems:
                if alp >= problem[0] and cop >= problem[1]:
                    nxt_cost = cost+problem[4]
                    nxt_alp = alp+problem[2]
                    if nxt_alp >= target[0]:
                        nxt_alp = target[0]
                        chk = True
                    if dp[nxt_alp][target[1]] > nxt_cost:
                        dp[nxt_alp][target[1]] = nxt_cost
                        queue.append((nxt_alp, target[1]))
        elif alp >= target[0] and cop < target[1]:
            for problem in cop_problems:
                if alp >= problem[0] and cop >= problem[1]:
                    nxt_cost = cost+problem[4]
                    nxt_cop = cop+problem[3]
                    if nxt_cop >= target[1]:
                        nxt_cop = target[1]
                        chk = True
                    
                    if dp[target[0]][nxt_cop] > nxt_cost:
                        dp[target[0]][nxt_cop] = nxt_cost
                        queue.append((target[0], nxt_cop))
    
    return dp[-1][-1]