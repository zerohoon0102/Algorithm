def bubble_sort(n_arr):
    n = 0
    max_len = len(n_arr)
    while( n < max_len ):
        tmp_idx = n
        while( tmp_idx < max_len - 1 ):
            if n_arr[tmp_idx] > n_arr[tmp_idx+1]:
                tmp_value = n_arr[tmp_idx]
                n_arr[tmp_idx] = n_arr[tmp_idx+1]
                n_arr[tmp_idx+1] = tmp_value
            tmp_idx += 1
        max_len -= 1
    print(n_arr)



# Time Complexity: O(n*n)
# Worst Sort-Algorithm