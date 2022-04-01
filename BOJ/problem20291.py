import sys
from collections import Counter

N = int(sys.stdin.readline())

arr = [sys.stdin.readline().rstrip().split('.')[1] for _ in range(N)]
count = Counter(arr)
for key in sorted(count):
    print(f"{key} {count[key]}")
