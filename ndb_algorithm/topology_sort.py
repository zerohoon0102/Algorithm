n = 7
def topologySort(inDegree, fromTo):
    result = []
    queue = []
    for i in range(0, n):
        if inDegree[i] == 0:
            queue.append(i)
    for i in range(0, n):
        if(len(queue) == 0):
            print("싸이클이 존재합니다.")
            return 0
        x = queue.pop(0)
        result.append(x)
        for end in fromTo[x]:
            inDegree[end] -= 1
            if inDegree[end] == 0:
                queue.append(end)


if __name__=="__main__":
    fromTo = []
    inDegree = [0]*n
    fromTo.append([1,4])
    inDegree[1] += 1
    inDegree[4] += 1
    fromTo.append([2])
    inDegree[2] += 1
    fromTo.append([3])
    inDegree[3] += 1
    fromTo.append([5])
    inDegree[5] += 1
    fromTo.append([5])
    inDegree[5] += 1
    fromTo.append([6])
    inDegree[6] += 1
    fromTo.append([])
    topologySort(inDegree, fromTo)