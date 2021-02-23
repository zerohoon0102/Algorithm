def quick_sort(n_arr, start, end):
    if start < end:
        pivot = start
        i = start + 1
        j = end
        while( i < j):
            while( n_arr[i] <= n_arr[pivot] and i < end):
                i += 1
            while( n_arr[j] >= n_arr[pivot] and j > start):
                j -= 1
            if i < j:
                tmp_value = n_arr[i]
                n_arr[i] = n_arr[j]
                n_arr[j] = tmp_value
            else:
                tmp_value = n_arr[j]
                n_arr[j] = n_arr[pivot]
                n_arr[pivot] = tmp_value
        quick_sort(n_arr, start, j-1)
        quick_sort(n_arr, j+1, end)
    
# Time Complexity : O(n * log n)
# most fast sorting algorithm
# very slow especially almost sorted list