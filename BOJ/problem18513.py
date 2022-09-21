import sys
from collections import defaultdict

input = sys.stdin.readline    

N, K = map(int, input().rstrip().split())
water = list(map(int, input().rstrip().split()))
water.sort()
between = {}
idx = 0
for i in range(N-1):
    if water[i+1] - water[i] - 1 > 0:
        between[idx] = (water[i+1]-water[i] - 1)
        idx += 1

val = 1
result = 0
while K > 0:
    K -= 1
    result += val
    if K == 0:
        break
    K -= 1
    result += val
    if K == 0:
        break
    keys = tuple(between)
    for i in keys:
        if between[i] == 0:
            del between[i]
            continue
        between[i] -= 1
        K -= 1
        result += val
        if K == 0:
            break
        if between[i] > 0:
            between[i] -= 1
            K -= 1
            result += val
            if K == 0:
                break
    
    val += 1
print(result)
