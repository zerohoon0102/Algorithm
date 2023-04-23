import sys
from collections import deque

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

cycle = {}
def dfs(tmp_arr, tmp_chk, idx):
    nxt_idx = tmp_arr[idx]
    cycle[idx] = len(cycle)+1
    
    if (nxt_idx in tmp_chk) and tmp_chk[nxt_idx]:
        tmp_chk[nxt_idx] = False
        return dfs(tmp_arr, tmp_chk, nxt_idx)
    elif nxt_idx in cycle:
        exc = len(cycle)-cycle[nxt_idx]+1
        return exc
    return 0
        

T = int(input())

for _ in range(T):
    N = int(input())
    arr = map(int, input().rstrip().split())
    
    dic = {}
    chk = {}
    for i,v in enumerate(arr):
        i += 1
        if i != v:
            dic[i] = v
            chk[i] = True
        else:
            N -= 1
    
    for i in dic:
        if chk[i]:
            chk[i] = False
            N -= dfs(dic, chk, i)
            cycle = {}
    
    print(N)
