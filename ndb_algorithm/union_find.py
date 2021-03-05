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
    if getParent(node,n1) == getParent(node, n2):
        return True
    return False
