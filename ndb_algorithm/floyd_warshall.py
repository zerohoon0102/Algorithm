number = 4
INF = 2100000000

a = [[0,5,INF,8],
     [7,0,9,INF],
     [2,INF,0,4],
     [INF,INF,3,0]]

def floydWarshall():
    node_value = a.copy()
    for via in range(number):
        for start in range(number):
            if start != via:
                for end in range(number):
                    if (end != via) and (end != start):
                        if node_value[start][end] > node_value[start][via]+node_value[via][end]:
                            node_value[start][end] = node_value[start][via]+node_value[via][end]