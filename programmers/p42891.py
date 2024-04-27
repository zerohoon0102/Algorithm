from heapq import heappush, heappop

# 처음 생각한 알고리즘은 1->n 까지 루프를 돌면서 turn이 k가 될 때까지 진행하는 방식을 생각
# 하지만, 해당 방식은 2 x 10^13 이라는 시간 복잡도를 만족할 수 없음
# 두 번째 생각한 알고리즘은 현재 남은 음식 중 가장 적게 남은 food time을 트래킹 하면서
# 해당 값 만큼 남은 음식 전체에 time을 빼면서 시간이 k가 될 때까지 진행하는 방식을 생각
# 해당 방식의 경우 k의 값과 상관없이 n=200,000을 갖는 O(n)을 만족함
def solution(food_times, k):
    if sum(food_times) <= k:
        # 음식의 총 양보다 k가 같거나 크면 더 이상 먹을 음식이 없는 상황이 오게 됨.
        return -1
    rest_food_len = len(food_times)
    foods_info = [True]*rest_food_len
    times_asc_list = []
    chk = {}
    for idx, food_time in enumerate(food_times):
        if food_time not in chk:
            chk[food_time] = [idx]
            heappush(times_asc_list, food_time)
        else:
            chk[food_time].append(idx)
    
    turn = 0
    prev_time = 0
    cur_time = 0
    while turn <= k:
        prev_time = cur_time
        cur_time = heappop(times_asc_list)
        diff = cur_time-prev_time

        if diff*rest_food_len + turn < k:
            # k가 가장 양이 적게 남은 음식을 지우기에 충분한 경우
            ## 양이 가장 적게 남은 음식들을 지우고, turn을 증가시킴.
            turn += rest_food_len*diff
            rest_food_len -= len(chk[cur_time])
            for idx in chk[cur_time]:
                foods_info[idx] = False
        else:
            # k가 가장 양이 적게 남은 음식을 지우기에 충분하지 않은 경우
            # 남은 음식 중 어떤 음식이 다음에 먹을 음식인지 탐색
            rest_turn = k - turn
            rest_turn %= rest_food_len
            idx = 0
            while 1:
                if foods_info[idx]:
                    rest_turn -= 1
                idx += 1
                if rest_turn == -1:
                    return idx
