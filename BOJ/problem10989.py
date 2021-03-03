import sys

N = int(sys.stdin.readline())
n_arr = [0,]*10001

for _ in range(N):
    n_arr[int(sys.stdin.readline())] += 1

for i in range(10001):
    if n_arr[i] != 0:
        print(str(i) + ("\n" + str(i)) * (n_arr[i] - 1))
