def selection_sort(n_arr):
    n = 0
    max_len = len(n_arr)
    while( n < max_len):
        tmp_min = n
        loop_num = n
        while( loop_num < max_len):
            if n_arr[tmp_min] > n_arr[loop_num]:
                tmp_min = loop_num
            loop_num += 1
        n_value = n_arr[n]
        n_arr[n] = n_arr[tmp_min]
        n_arr[tmp_min] = n_value
        n = n+1
    
    print(n_arr)
