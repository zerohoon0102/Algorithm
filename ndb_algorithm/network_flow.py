MAX = 100
INF = 2100000000

n = 6
c = [[0]*MAX]*MAX
f = [[0]*MAX]*MAX
d = [-1]*MAX

a = [[]]*MAX

def maxFlow(start, end):
    result = 0
    while(1):
        d = [-1]*MAX
        queue = []
        queue.append(start)
        while(len(queue) > 0):
            x = queue.pop(0)
            for i in range(len(a[x])):
                y = a[x][i]
                if ((c[x][y] - f[x][y] > 0) and (d[y] == -1)):
                    queue.append(y)
                    d[y] = x
                    if y == end:
                        break
        if d[end] == -1:
            break
        flow = INF
        j = end
        while(j != start):
            flow = min(flow, c[d[j]][j] - f[d[j]][j])
            j = d[j]
        
        j = end
        while(j != start):
            f[d[j]][j] += flow
            f[j][d[j]] -= flow
            j = d[j]
        result += flow
    return result

if __name__=="__main__":
    a[1].append(2)
    a[2].append(1)
    c[1][2] = 12

    a[1].append(4)
    a[4].append(1)
    c[1][4] = 11

    a[2].append(3)
    a[3].append(2)
    c[2][3] = 6

    a[2].append(4)
    a[4].append(2)
    c[2][4] = 3

    a[2].append(5)
    a[5].append(2)
    c[2][5] = 5

    a[2].append(6)
    a[6].append(2)
    c[2][6] = 9

    a[3].append(6)
    a[6].append(3)
    c[3][6] = 8

    a[4].append(5)
    a[5].append(4)
    c[4][5] = 9

    a[5].append(3)
    a[3].append(5)
    c[5][3] = 3

    a[5].append(6)
    a[6].append(5)
    c[5][6] = 4
    result = maxFlow(1,6)
    print(result)