import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
result = 0

def factorial_v2(value, end):
    v = 1
    tmp = 0
    while end > tmp and value > 0:
        v *= value
        value -= 1
        tmp += 1
    return v

k = K
zero = 0
if K > N:
    zero = K-N
    k = N

while k > 0:
    case = factorial_v2(N-1, k-1)//factorial_v2(k-1, k-1)
    multi = factorial_v2(K, K)//(factorial_v2(zero, zero)*factorial_v2(k,k))
    result += case*multi
    result %= 1000000000
    k -= 1
    zero += 1

print(result)
