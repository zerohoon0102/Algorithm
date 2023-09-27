class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        total = sum(matchsticks)
        if total%4 > 0:
            return False

        one_side = total//4
        length = len(matchsticks)
        used = [False]*len(matchsticks)

        def dfs(idx, cnt, cur):
            result = False
            if cnt == 4:
                return True
            for i in range(idx, length):
                if used[i] or (i and not used[i-1] and matchsticks[i-1] == matchsticks[i]):
                    continue
                nxt_v = cur+matchsticks[i]
                if nxt_v > one_side:
                    continue
                else:
                    used[i] = True
                    if nxt_v == one_side:
                        result = dfs(0, cnt+1, 0)
                    else:
                        result = dfs(i+1, cnt, nxt_v)
                    if result:
                        return True
                    used[i] = False
            return result

        return dfs(0, 0, 0)
    
