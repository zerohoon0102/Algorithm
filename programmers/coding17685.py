def solution(words):
    answer = 0
    info = {}
    for word in words:
        idx = 0
        cur = info
        while 1:
            s = word[idx]
            if s not in cur:
                cur[s] = {0: word[idx+1:]}
                break
            else:
                if len(cur[s]) == 1:
                    if 0 in cur[s]:
                        if len(cur[s][0]) > 0:
                            tmp = cur[s][0]
                            del cur[s][0]
                            cur[s][tmp[0]] = {0: tmp[1:]}
                if idx == len(word)-1:
                    cur[s][0] = ""
                    break
                cur = cur[s]
            idx += 1
    def dfs(info_t, n):
        result = 0
        for a in info_t:
            if a == 0:
                result += n
            else:
                result += dfs(info_t[a], n+1)
        return result
    answer = dfs(info, 0)
    return answer