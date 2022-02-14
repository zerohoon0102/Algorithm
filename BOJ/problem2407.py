import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

if m > n//2:
    m = n-m

result = 1
for i in range(n, n-m, -1):
    result *= i
    while m > 0 and result%m == 0:
        result //= m
        m -= 1

print(result)
