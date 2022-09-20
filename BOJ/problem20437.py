import sys
from collections import defaultdict

input = sys.stdin.readline    

T = int(input())
for _ in range(T):
    W = input().rstrip()
    K = int(input())
    s_dict = defaultdict(list)
    result_a = 10001
    result_b = 0
    for i,w in enumerate(W):
        s_dict[w].append(i)
        if len(s_dict[w]) >= K:
            result_a = min(result_a, s_dict[w][-1]-s_dict[w][-K])
            result_b = max(result_b, s_dict[w][-1]-s_dict[w][-K])
    if result_a == 10001:
        print(-1)
    else:
        print(result_a+1, result_b+1)
