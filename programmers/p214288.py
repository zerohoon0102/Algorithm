from heapq import heappop, heappush

def dfs(cur_type:int, rest_mentor:int, consult_info_list: list):
    cur_consult_info = consult_info_list[cur_type]
    result = 10000000
    for num_mentor in range(1, min(rest_mentor+1, max(cur_consult_info))+1):
        cur_wait_time = cur_consult_info[num_mentor]
        if cur_type+1 == len(consult_info_list):
            result = min(result, cur_wait_time)
        else:
            result = min(result, cur_wait_time + dfs(cur_type+1, rest_mentor-num_mentor+1, consult_info_list))
    print(cur_type, result)
    return result

def solution(k, n, reqs):
    answer = 1000000
    K = k
    
    consult_lists = [[] for _ in range(k+1)]
    for a, b, c in reqs:
        consult_lists[c].append((a, b))
    
    consult_info = [{} for _ in range(k+1)]
    for consult_type in range(1, k+1):
        cur_consult_list = consult_lists[consult_type]
        cur_consult_info = consult_info[consult_type]
        for mentor_num in range(1, n-k+2):
            end_timerest = []
            chk = False
            wait_time = 0
            for a, b in cur_consult_list:
                while end_timerest and end_timerest[0] <= a:
                    heappop(end_timerest)
                if len(end_timerest) < mentor_num:
                    heappush(end_timerest, a+b)
                else:
                    last_end = heappop(end_timerest)
                    chk = True
                    wait_time += last_end - a
                    heappush(end_timerest, last_end+b)
            cur_consult_info[mentor_num] = wait_time
            if chk == False:
                break
    
    answer = dfs(cur_type=1, rest_mentor=n-k, consult_info_list=consult_info)
    return answer
