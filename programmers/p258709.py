from itertools import combinations

# O(6**N), 1 <= N <= 5
def dfs(scores, dice_info, dices, idx, value, try_num):
    cur_dice = dices[idx]
    cur_dice_info = dice_info[cur_dice]
    for v, t in cur_dice_info.items():
        nxt_v = v+value
        nxt_t = t*try_num
        if idx == len(dices)-1:
            if nxt_v not in scores:
                scores[nxt_v] = nxt_t
            else:
                scores[nxt_v] += nxt_t
        else:
            dfs(scores, dice_info, dices, idx+1, nxt_v, nxt_t)

# O(6**N) + O(L)+O(R), 1 <= N <= 5, 0 < L <= 500, 0 < R <= 500
def count_win_number(l_dices, r_dices, dice_info):
    l_scores = {}
    r_scores = {}
    
    dfs(l_scores, dice_info, l_dices, 0, 0, 1)
    dfs(r_scores, dice_info, r_dices, 0, 0, 1)
    
    result = 0
    mid = 0
    l_idx, r_idx = 0, 0
    l_value_list, r_value_list = sorted(l_scores), sorted(r_scores)
    r_total_try = 0
    
    while l_idx < len(l_value_list):
        l_v = l_value_list[l_idx]
        l_t = l_scores[l_v]
        while r_idx < len(r_value_list):
            r_v = r_value_list[r_idx]
            r_t = r_scores[r_v]
            if l_v <= r_v:
                if l_v == r_v:
                    mid += l_t*r_t
                break
            r_total_try += r_t
            r_idx += 1
                
        result += r_total_try*l_t
        l_idx += 1
    
    return result, 6**(2*len(l_dices))-result-mid

# C(d, 2) * (O(6**N) + O(L)+O(R)) | 2 <= d <= 10,  1 <= N <= 5, 0 < L <= 500, 0 < R <= 500
def solution(dice):
    answer = []
    dice_num = len(dice)
    dice_info = {idx: {} for idx in range(dice_num)}
    for idx in range(dice_num):
        for v in dice[idx]:
            if v not in dice_info[idx]:
                dice_info[idx][v] = 1
            else:
                dice_info[idx][v] += 1
    
    cur = 0
    chk = {}
    for combs in combinations(range(dice_num),dice_num//2):
        l_dices = sorted(combs)
        l_dices_str = "".join(map(str, l_dices))
        if l_dices_str in chk:
            continue
        r_dices = []
        for i in range(dice_num):
            if i not in l_dices:
                r_dices.append(i)
        chk["".join(map(str, r_dices))] = True
        
        l_win, r_win = count_win_number(l_dices, r_dices, dice_info)
        if l_win > cur:
            cur = l_win
            answer = l_dices
        if r_win > cur:
            cur = r_win
            answer = r_dices
    
    for i in range(dice_num//2):
        answer[i] += 1
    return answer
