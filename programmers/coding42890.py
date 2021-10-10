import itertools

def solution(relation):
    answer = 0
    
    col_len = len(relation[0])
    col_list = []
    iter_str = ''
    for int_sample in range(0, col_len):
        iter_str = iter_str + f"{int_sample}"
    for sel_num in range(1, col_len + 1):
        col_list.append(list(itertools.combinations(iter_str, sel_num)))
    for num_col in col_list:
        for sel_col in num_col:
            temp_list = []
            test = True
            for row in range(0, len(relation)):
                temp_str = ''
                for int_str in sel_col:
                    temp_str = temp_str + ',' + relation[row][int(int_str)]
                if temp_str in temp_list:
                    test = False
                    break
                else:
                    temp_list.append(temp_str)
            if test:
                answer += 1
                for ns in range(0, len(col_list)):
                    temp_del_list = []
                    for ds in range(0, len(col_list[ns])):
                        if set(sel_col).issubset(set(col_list[ns][ds])):
                            temp_del_list.append(ds)
                    for tds in range(0, len(temp_del_list)):
                        if col_list[ns][temp_del_list[tds]] != sel_col:
                            del col_list[ns][temp_del_list[tds]]
                        for tds_idx in range(tds + 1, len(temp_del_list)):
                            temp_del_list[tds_idx] = temp_del_list[tds_idx] - 1
    return answer