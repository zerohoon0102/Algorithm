import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

S = list(map(int, sys.stdin.readline().rstrip().split()))

num_arr = []
even = 0
for s in S:
    if s%2 == 0:
        if even >= 0:
            even += 1
        else:
            if len(num_arr) > 0:
                num_arr.append(even)
            even = 1
    else:
        if even <= 0:
            even -= 1
        else:
            num_arr.append(even)
            even = -1
if even > 0:
    num_arr.append(even)

start = 0
end = 0
rest = K
cur = 0
result = 0
chk = False

while end < len(num_arr):
    while rest + num_arr[end] >= 0:
        if num_arr[end] > 0:
            cur += num_arr[end]
            if result < cur:
                result = cur
        else:
            rest += num_arr[end]
        end += 1
        if end == len(num_arr):
            chk = True
            break
    if chk:
        break
    while (end < len(num_arr)) and (rest + num_arr[end] < 0):
        if num_arr[start] > 0:
            cur -= num_arr[start]
        else:
            rest -= num_arr[start]
        start += 1

print(result)

# 홀수와 짝수의 연속을 담은 배열 생성 O(N)
# 홀수와 짝수의 연속을 담은 배열을 탐색 O(N)
# ==> O(N)