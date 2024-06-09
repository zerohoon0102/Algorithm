# 후기 먼저!
# 푸는데 너무 오래 걸렸다...3번째 테스트 케이스에서 계속 틀렸다.
# 풀이 이후 다른 사람들의 풀이를 확인해본 결과 대부분 DP인 것으로 확인되지만, 내 머릿 속에서는 압축된 정보와 정해진 규칙 아래에 0인 구간 1인 구간을 처리하는 로직만
# 계속 떠올랐다. 다른 경우의 수를 거칠 필요가 없었기 때문에 보다 나은 시간 복잡도를 갖고 있다 생각했다.
# 마지막 탑승에서 특정 케이스를 생각하지 못 해서, 그 케이스에 한 6시간은 사용한 것 같다.
# [ 풀이 ]
# 0인 구간과 1인 구간을 각각 길이로 치환한다, [0,0,0,1,1,0,1] -> [3,2,1,1]
# 탑승하는 구간과 탑승하지 않은 구간은 각각 짝수 번째, 홀수 번째에 위치해 있다.
# 해당 문제는 에어컨을 꺼서 temperature에서 시간을 소모하는 경우의 수와 항상 쾌적한 실내 온도 t1(or t2) +- 1 을 항상 유지하는 경우의 수가 있다.
# 에어컨을 꺼서 temperature에서 시간을 소모하는 것이 더 이득인 경우만 잘 생각해주면 문제는 쉬워진다.
# 위 조건들에 추가적으로 아래의 변화에서 나올 수 있는 경우의 수를 조건문으로 처리하면 풀이가 된다.
# 1. 미탑승 -> 탑승 : 탑승으로 넘어갈 때, t1(or t2)나 t1+1(or t2-1)인 경우
# 2. 탑승 -> 미탑승 : 미탑승으로 넘어갈 때, t1(or t2)나 t1-1(or t2+1)인 경우
# 3. 마지막 탑승 : 마지막 탑승 구간의 마지막 탑승 시간은 고려 x
# 4. 2*b >= a 이면 t1(or t2)일 때, 계속 쾌적한 실내온도를 유지하기 위해서 a를 이용하는게 이득이고 그렇지 않으면 b가 이득이다.
# 시간 복잡도는 O(N). 공간 복잡도는 {onboard길이}*2 언저리이다.
def solution(temperature, t1, t2, a, b, onboard):
    answer = 0
    board_info = []
    cur = 0
    for cur_b in onboard:
        if cur_b:
            if cur < 0:
                board_info.append(-cur)
                cur = 1
            else:
                cur += 1
        else:
            if cur > 0:
                board_info.append(cur)
                cur = -1
            else:
                cur -= 1
    if cur > 0:
        board_info.append(cur)
    chk_a_is_benefit = True if 2*b >= a else False
    
    cur_t = temperature
    target_t = t1 if temperature < t1 else t2
    target_t_under = t1 - 1 if temperature < t1 else t2 + 1
    target_t_over = t1 + 1 if temperature < t1 else t2 - 1
    
    for idx in range(len(board_info)):
        used_watt = 0
        nxt_t = cur_t
        arc_board_info = board_info[idx]
        if nxt_t == target_t_over:
            if board_info[idx] == 1 and idx == len(board_info) - 1:
                if b < a:
                    nxt_t = target_t
                    answer += (b-a)
            else:
                board_info[idx] -= 1
                nxt_t = target_t
        if not (t1 <= nxt_t <= t2):
            used_watt += abs(target_t - nxt_t)*a
            board_info[idx] -= abs(target_t - nxt_t)
            nxt_t = target_t
        
        if board_info[idx] and idx == len(board_info)-1:
            board_info[idx] -= 1
        
        if board_info[idx]:
            if board_info[idx]%2 == 1 and idx == len(board_info)-1:
                used_watt += min(a,b)
                board_info[idx] -= 1
            if chk_a_is_benefit:
                if idx%2 == 1 and board_info[idx] % 2 == 1:
                    nxt_t = target_t_under
                if idx%2 == 0 and board_info[idx] % 2 == 1:
                    nxt_t = target_t_over
                    used_watt += a
                used_watt += a*(board_info[idx]//2)
            else:
                used_watt += b*(board_info[idx])
        
        if idx%2 == 0 and a*abs(target_t - temperature) <= used_watt and ((
             not (cur_t == target_t_under and cur_t == target_t) and abs(cur_t - temperature) + abs(target_t - temperature) <= arc_board_info) or (
             cur_t == target_t and abs(target_t - temperature) + abs(target_t - temperature) <= arc_board_info) or
             ((cur_t == target_t_under or (cur_t == target_t and ((chk_a_is_benefit and a > b) or not chk_a_is_benefit)) )and abs(target_t_under - temperature) + abs(target_t - temperature) <= arc_board_info)):
            answer += a*abs(target_t - temperature)
            if cur_t == target_t:
                if chk_a_is_benefit:
                    if a > b:
                        answer += (b-a)
                else:
                    answer -= b
            cur_t = target_t
        else:
            answer += used_watt
            cur_t = nxt_t
    return answer
