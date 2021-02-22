def insertion_sort(n_arr):
    n = 1
    max_len = len(n_arr)
    while( n < max_len ):
        tmp_n = n
        while( tmp_n >= 1 ):
            if n_arr[tmp_n - 1] > n_arr[tmp_n]:
                tmp_value = n_arr[tmp_n - 1]
                n_arr[tmp_n - 1] = n_arr[tmp_n]
                n_arr[tmp_n] = tmp_value
            tmp_n -= 1
        n += 1
    print(n_arr)

# Time Complexity : O(n*n)
# very fast especially almost sorted list