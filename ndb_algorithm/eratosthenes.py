n = [True]*5001

def eratosthenes(n_arr):
    for i in range(2, len(n_arr)):
        if n_arr[i] == True:
            print(i)
            tmp_num = 2 * i
            while(tmp_num < len(n_arr)):
                n_arr[tmp_num] = False
                tmp_num += i
if __name__=="__main__":
    eratosthenes(n)