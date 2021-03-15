number = 6
INF = 2100000000

n_arr = [
    [0,2,5,1,INF,INF],
    [2,0,3,2,INF,INF],
    [5,3,0,3,1,5],
    [1,2,3,0,1,INF],
    [INF,INF,1,1,0,2],
    [INF,INF,5,INF,2,0]]

node_chk = [0,1,2,3,4,5]
node_value = [INF]*number

start_node = 0
cur_node = start_node
node_value[start_node] = 0

while(len(node_chk) > 0):
    node_chk.remove(cur_node)
    for idx in range(len(n_arr[cur_node])):
        if (idx in node_chk) and n_arr[cur_node][idx] != INF:
            if node_value[idx] > (node_value[cur_node] + n_arr[cur_node][idx]):
                node_value[idx] = n_arr[cur_node][idx] + node_value[cur_node]
                
    min_node = -1
    min_value = INF
    for idx in node_chk:
        if min_value >= node_value[idx]:
            min_value = node_value[idx]
            min_node = idx
    
    cur_node = min_node
print(node_value)