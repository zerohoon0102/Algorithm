def merge(n_arr, start, mid, end):
    tmp_arr = [0,]*(end-start + 1)
    i = start
    j = mid + 1
    k = 0
    while( k <= end ):
        if n_arr[i] < n_arr[j]:
            tmp_arr[k] = n_arr[i]
            i += 1
        else:
            tmp_arr[k] = n_arr[j]
            j += 1
        k += 1
        if i > mid:
            tmp_arr[k:end+1] = n_arr[j:end+1]
            break
        elif j > end:
            tmp_arr[k:end+1] = n_arr[i:mid+1]
            break;
    n_arr[start:end+1] = tmp_arr

def merge_sort(n_arr, start, end):
    if start < end:
        mid = int((start + end) / 2)
        merge_sort(n_arr, 0, mid)
        merge_sort(n_arr, mid+1, end)
        merge(n_arr, start, mid, end)


if __name__ == "__main__":
    n_arr = [7,4,2,1,8,3,6,5,9]
    merge_sort(n_arr, 0, len(n_arr) - 1)

# Time Complexity : O(n * log n) is secure