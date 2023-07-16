import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def get_parent(v, arr):
    parent = arr[v]
    if parent != v:
        arr[v] = get_parent(parent, arr)
    return arr[v]

robot_cnt = defaultdict(lambda:1)
part = {}
N = int(input())

for _ in range(N):
    cmd = input().rstrip().split()
    if cmd[0] == "I":
        a, b = map(int, cmd[1:])
        if a in part:
            A = get_parent(a, part)
        else:
            A = a
            part[a] = a
        if b in part:
            B = get_parent(b, part)
        else:
            B = b
            part[b] = b
        
        if A < B:
            robot_cnt[A] += robot_cnt[B]
            part[B] = part[A]
        elif A > B:
            robot_cnt[B] += robot_cnt[A]
            part[A] = part[B]
    else:
        c = int(cmd[1])
        if c not in part:
            print(1)
        else:
            print(robot_cnt[get_parent(c, part)])
