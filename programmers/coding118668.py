from collections import deque

def solution(alp, cop, problems):
    answer = 100000
    problems.append([0,0,0,1,1])
    problems.append([0,0,1,0,1])
    alp_problems = sorted(problems, key=lambda x: -(x[2]/x[4]))
    cop_problems = sorted(problems, key=lambda x: -(x[3]/x[4]))
    problems.sort(key=lambda x: (-(x[2]+x[3])/x[4], x[4]))
    print(alp_problems)
    print(cop_problems)
    print(problems)
    dp = [[100000000]*301 for _ in range(301)]
    dp[alp][cop] = 0
    target = [0,0]
    for problem in problems:
        target[0] = max(target[0], problem[0])
        target[1] = max(target[1], problem[1])
    
    queue = deque([(alp,cop)])
    while queue:
        alp, cop = queue.popleft()
        cost = dp[alp][cop]
        if alp >= target[0] and cop >= target[1]:
            answer = min(answer, cost)
            continue
        if alp < target[0] and cop < target[1]:
            for problem in problems:
                if alp >= problem[0] and cop >= problem[1]:
                    nxt_cost = cost+problem[4]
                    nxt_alp = alp+problem[2]
                    nxt_cop = cop+problem[3]
                    if dp[nxt_alp][nxt_cop] > nxt_cost:
                        dp[nxt_alp][nxt_cop] = nxt_cost
                        queue.append((nxt_alp, nxt_cop))
        if alp < target[0]:
            for problem in alp_problems:
                if alp >= problem[0] and cop >= problem[1]:
                    nxt_cost = cost+problem[4]
                    nxt_alp = alp+problem[2]
                    nxt_cop = cop+problem[3]
                    break
            nxt_alp = min(nxt_alp, 300)
            if dp[nxt_alp][nxt_cop] > nxt_cost:
                dp[nxt_alp][nxt_cop] = nxt_cost
                queue.append((nxt_alp, nxt_cop))
        if cop < target[1]:
            for problem in cop_problems:
                if alp >= problem[0] and cop >= problem[1]:
                    nxt_cost = cost+problem[4]
                    nxt_alp = alp+problem[2]
                    nxt_cop = cop+problem[3]
                    break
            nxt_cop = min(nxt_cop, 300)
            if dp[nxt_alp][nxt_cop] > nxt_cost:
                dp[nxt_alp][nxt_cop] = nxt_cost
                queue.append((nxt_alp, nxt_cop))
    
    return answer