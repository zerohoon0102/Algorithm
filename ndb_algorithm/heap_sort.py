def heapify(n_arr, length):
    for i in range(1, length):
        c = i
        while(1):
            root = int((c - 1)/2)
            if n_arr[root] < n_arr[c]:
                temp = n_arr[root]
                n_arr[root] = n_arr[c]
                n_arr[c] = temp
            c = root
            if( c == 0 ):
                break

def reheapify(n_arr, length):
    root = 0
    while(1):
        c = 2*root + 1
        if c < length - 1 and n_arr[c] < n_arr[c+1]:
            c += 1
        if n_arr[root] < n_arr[c]:
            temp = n_arr[root]
            n_arr[root] = n_arr[c]
            n_arr[c] = temp
        root = c
        if ( 2*root + 1 >= length ):
            break
    return n_arr
            


def heap_sort(n_arr):
    length = len(n_arr)
    heapify(n_arr, length)
    while( length > 1 ):
        temp = n_arr[0]
        n_arr[0] = n_arr[length-1]
        n_arr[length-1] = temp
        length -= 1
        if length > 1:
            n_arr[0:length] = reheapify(n_arr[0:length], length)
    print(n_arr)

if __name__ == "__main__":
    heap_sort([4,2,1,3,6])