def getParent(node, n):
    if node[n] == n:
        return n
    node[n] = getParent(node, node[n])
    return node[n]

def unionParent(node, n1, n2):
    if node[n1] != n1:
        n1 = getParent(node, n1)
    if node[n2] != n2:
        n2 = getParent(node, n2)
    if n1 > n2:
        node[n1] = n2
    else:
        node[n2] = n1

def findParent(node, n1, n2):
    t = getParent(node, n1)
    f = getParent(node, n2)
    if t == f:
        return True
    return False

class Edge:
    def __init__(self, point1, point2, distance):
        self.point1 = point1
        self.point2 = point2
        self.distance = distance

def kruskal(node, edge_list):
    cost = 0
    edge_list.sort(key=lambda x:x.distance)
    for edge in edge_list:
        if findParent(node, edge.point1, edge.point2) == False:
            unionParent(node, edge.point1, edge.point2)
            cost += edge.distance
    print(cost)
    
if __name__=="__main__":
    n = 7
    m = 11

    v = []
    v.append(Edge(1,7,12))
    v.append(Edge(1,4,28))
    v.append(Edge(1,2,67))
    v.append(Edge(1,5,17))
    v.append(Edge(2,4,24))
    v.append(Edge(2,5,62))
    v.append(Edge(3,5,20))
    v.append(Edge(3,6,37))
    v.append(Edge(4,7,13))
    v.append(Edge(5,6,45))
    v.append(Edge(5,7,73))
    parent = [0]*8
    for i in range(1,8):
        parent[i] = i
    kruskal(parent, v)