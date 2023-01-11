import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
n_s = input().rstrip()

minus = 0
cur = 1
left = 0
prev_n = n_s[0]
result = [n_s[0]]

while cur < N:
    n = n_s[cur]
    if n > prev_n:
        while result and result[-1] < n and minus < K:
            result.pop()
            minus += 1
    result.append(n)
    prev_n = n
    cur += 1
rest = len(result) - (K-minus)
result = result[:rest]
print(''.join(result))
