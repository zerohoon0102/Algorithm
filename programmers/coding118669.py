from collections import deque

def solution(n, paths, gates, summits):
    INF = 10**7+1
    answer = [INF, INF]
    
    path_info = [{} for _ in range(n+1)]
    
    for path in paths:
        s, e, v = path
        path_info[s][e] = v
        path_info[e][s] = v
    
    dp = [INF]*(n+1)
    for g in gates:
        dp[g] = 0
    
    for s in summits:
        dp[s] = -1
    
    queue = deque(gates)
    while queue:
        c = queue.popleft()
        for nxt in path_info[c]:
            if dp[nxt] == -1:
                if max(dp[c], path_info[c][nxt]) < answer[1]:
                    answer[1] = max(dp[c], path_info[c][nxt])
                    answer[0] = nxt
                elif max(dp[c], path_info[c][nxt]) == answer[1]:
                    answer[0] = min(answer[0], nxt)
            else:
                if max(dp[c], path_info[c][nxt]) < dp[nxt]:
                    queue.append(nxt)
                    dp[nxt] = max(dp[c], path_info[c][nxt])
                
    return answer