import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

class Node:
    def __init__(self, i, bef, aft):
        self.bef = bef
        self.aft = aft
        self.num = i

num = 0
first = None
last = None
for _ in range(N):
    cmd = sys.stdin.readline().rstrip()
    if cmd == "back":
        if last == None:
            print(-1)
        else:
            print(last.num)
    elif cmd == "front":
        if first == None:
            print(-1)
        else:
            print(first.num)
    elif cmd == "empty":
        print(int(first==None))
    elif cmd == "size":
        print(num)
    elif cmd == "pop_back":
        if last == None:
            print(-1)
        else:
            print(last.num)
            if first==last:
                first = None
            else:
                last.bef.aft = None
            last = last.bef
            num -= 1
    elif cmd == "pop_front":
        if first == None:
            print(-1)
        else:
            print(first.num)
            if first==last:
                last = None
            else:
                first.aft.bef = None
            first = first.aft
            num -= 1
    else:
        cmd, value = cmd.split()
        value = int(value)
        num += 1
        if cmd == "push_back":
            new_node = Node(value, last, None)
            if last == None:
                first = new_node
            else:
                last.aft = new_node
            last = new_node
        elif cmd == "push_front":
            new_node = Node(value, None, first)
            if first == None:
                last = new_node
            else:
                first.bef = new_node
            first = new_node
