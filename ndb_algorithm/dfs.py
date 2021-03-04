chk = []

def dfs(n_arr, n):
    if n in chk:
        return
    chk.append(n)
    for i in n_arr[n]:
        dfs(n_arr, i)


if __name__ == "__main__":
    n_arr = [0]*8
    n_arr[1] = [2,3]
    n_arr[2] = [1,3,4,5]
    n_arr[3] = [1,2,6,7]
    n_arr[4] = [2,5]
    n_arr[5] = [2,4]
    n_arr[6] = [3,7]
    n_arr[7] = [3,6]
    dfs(n_arr, 1)
    print(chk)