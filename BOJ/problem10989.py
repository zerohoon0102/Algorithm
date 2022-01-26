import sys

N = int(sys.stdin.readline().rstrip())

result = [0,]*10000
for _ in range(N):
    result[int(sys.stdin.readline().rstrip())-1] += 1

for i in range(10000):
    for _ in range(result[i]):
        print(i+1)


