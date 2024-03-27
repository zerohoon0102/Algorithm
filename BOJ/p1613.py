import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
info = [[0]*(n+1) for _ in range(n+1)]
chk = [True]*(n+1)
forward_back = [set() for _ in range(n+1)]

for _ in range(k):
    pre_act, aft_act = map(int, input().rstrip().split())
    info[pre_act][aft_act] = 1
    forward_back[pre_act].add(aft_act)

s = int(input())

def dfs(cur_n):
    if chk[cur_n] == True:
        chk[cur_n] = False
        for aft in forward_back[cur_n]:
            dfs(aft)
    
        for aft in list(forward_back[cur_n]):
            for aft_aft in forward_back[aft]:
                if not info[cur_n][aft_aft]:
                    info[cur_n][aft_aft] = 1
                    forward_back[cur_n].add(aft_aft)

result = []
for _ in range(s):
    pre_act, aft_act = map(int, input().rstrip().split())
    
    if info[pre_act][aft_act]:
        result.append('-1')
    elif info[aft_act][pre_act]:
        result.append('1')
    else:
        if chk[pre_act]:
            dfs(pre_act)
        if info[pre_act][aft_act]:
            result.append('-1')
        else:
            if chk[aft_act]:
                dfs(aft_act)
            if info[aft_act][pre_act]:
                result.append('1')
            else:
                result.append('0')
print("\n".join(result))
