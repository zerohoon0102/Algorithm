
def bfs(n, n_arr):
    queue = [n]
    chk = []
    while(len(queue) != 0):
        node = queue.pop(0)
        for i in n_arr[node]:
            if (i not in chk) and (i not in queue):
                queue.append(i)
        chk.append(node)
    print(chk)

if __name__ == "__main__":
    n_arr = [[]]*8
    n_arr[1] = [2,3]
    n_arr[2] = [1,3,4,5]
    n_arr[3] = [1,2,6,7]
    n_arr[4] = [2,5]
    n_arr[5] = [2,4]
    n_arr[6] = [3,7]
    n_arr[7] = [3,6]
    bfs(1, n_arr)