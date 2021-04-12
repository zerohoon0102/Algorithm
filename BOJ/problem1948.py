import sys
MAX = 10000


class Node:
    max_route = 0
    degree = 0

    def __init__(self):
        self.cross_line_right = []
        self.cross_line_reverse = []


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
node_list = [Node() for i in range(n)]

result = []

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    node_list[a-1].cross_line_right.append([b-1, c])
    node_list[b-1].cross_line_reverse.append([a-1, c])
    node_list[b-1].degree += 1
start, end = map(int, sys.stdin.readline().split())
queue = [start-1]

while(len(queue) > 0):
    cur_node = queue.pop(0)
    for cross in node_list[cur_node].cross_line_right:
        dest = cross[0]
        node_list[dest].max_route = max(
            node_list[dest].max_route, node_list[cur_node].max_route + cross[1]
        )
        node_list[dest].degree -= 1
        if node_list[dest].degree == 0:
            queue.append(dest)

queue = [end - 1]
while(len(queue) > 0):
    cur_node = queue.pop(0)
    for cross in node_list[cur_node].cross_line_reverse:
        dest = cross[0]
        if (node_list[dest].max_route == (node_list[cur_node].max_route - cross[1])):
            result.append((dest, cur_node))
            if node_list[dest].degree == 0:
                queue.append(dest)
                node_list[dest].degree -= 1

print(node_list[end-1].max_route)
print(len(set(result)))

