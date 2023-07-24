import sys

N = int(input())
K = int(input())

def get_count(num):
    div = 1
    count = 0
    while num//div > 0 and div <= N:
        count += min(num//div, N)
        div += 1
    return count

s = 1
e = min(N**2, 10**9)
result = 0
mid = (s+e)//2
while s < e:
    cnt = get_count(mid)
    if K > cnt:
        s = mid + 1
    elif K < cnt:
        e = mid
    else:
        e = mid
    mid = (s+e)//2
result = mid

print(result)
    
