import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    if n > m//2:
        n = m - n

    result = 1
    for _ in range(n):
        result *= m
        m -= 1
        while n > 0 and result%n == 0:
            result //= n
            n -= 1
    print(result)
