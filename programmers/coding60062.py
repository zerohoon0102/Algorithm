from itertools import permutations
def spare(n, weak, base_dist, result, check):
    for j in range(len(weak)):
        dist_list = permutations(base_dist, result)
        for tmp_dist in dist_list:
            weaks = weak[j:] + [x+n for x in weak[:j]]
            tmp_dist = list(tmp_dist)
            while( len(tmp_dist) > 0 ):
                dist = tmp_dist.pop()
                start = weaks[0]
                while(start + dist >= weaks[0]):
                    weaks.pop(0)
                    if len(weaks) == 0:
                        return result
    return -1

def solution(n, weaks, base_dist):
    sort_dist = sorted(base_dist, reverse=True)
    for i in range(1, len(base_dist)+1):
        tmp_dist = sort_dist[0:i].copy()
        t = spare(n, weaks.copy(), tmp_dist, i, [0]*len(weaks))
        if t > 0:
            return t
    return -1