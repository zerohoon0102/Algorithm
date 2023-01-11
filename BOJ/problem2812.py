import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
n_s = input().rstrip()

minus = 0
cur = 1
left = 0
prev_n = n_s[0]
result = n_s[0]

while cur < N:
    n = n_s[cur]
    if n > prev_n:
        i = 1
        while i <= len(result) and result[len(result)-i] < n and minus < K:
            minus += 1
            i += 1
        if i > 1:
            result = result[:len(result)-i+1]
    result += n
    prev_n = n
    cur += 1
rest = len(result) - (K-minus)
result = result[:rest]
print(result)
