def solution(coin, cards):
    answer = 1
    n = len(cards)
    target_n = n + 1
    
    # 2장의 카드를 더해서 n+1이 되어야 하기 때문에, 각 카듣 짝이 정해져 있음.
    # 처음 n//3 만큼의 카드를 뽑을 때, 짝이 없는 애들은 sel cards에 담아주고 짝이 나오면 낼 수 있는 카드 쌍을 +1 해줌.
    sel_cards = {}
    can_play_card_nums = 0
    for i in range(n//3):
        card = cards[i]
        sel_cards[card] = True
        if n-card+1 in sel_cards:
            can_play_card_nums += 1
            del sel_cards[card], sel_cards[n-card+1]
    
    # 카드들을 뽑아가면서 경우의 수를 찾게 되면, 케이스가 너무 많아짐. 언제 뽑는게 더 나은지 확신할 수 없기 때문.
    # 2장씩 확인하면서, 짝이 있으면 코인을 소모해서 낼 수 있는 쌍을 추가할 수 있다는 것만 체크하면 되는데
    # 이는 k 번째 라운드에서 더 이상 낼게 없으면, 이전에 코인을 소모하여 뽑았다고 치고 코인을 감소시키고 라운드를 진행하면 되기 때문.
    # 한 장만 새로 뽑아도 되는 경우가 더 유리하고, 두 장을 새로 뽑는 경우가 덜 유리하기 때문에 두 케이스를 분리하여 트래킹
    candidate_cards = {}
    can_play_candidate_card_list = {1:0, 2:0}
    for i in range(n//3, n, 2):
        for t in range(2):
            card = cards[i+t]
            candidate_cards[card] = True
            if n-card+1 in candidate_cards:
                can_play_candidate_card_list[2] += 1
                del candidate_cards[card], candidate_cards[n-card+1]
            if n-card+1 in sel_cards:
                can_play_candidate_card_list[1] += 1
                del candidate_cards[card], sel_cards[n-card+1]
        if can_play_card_nums > 0:
            can_play_card_nums -= 1
            answer += 1
        else:
            if coin > 0:
                if can_play_candidate_card_list[1] > 0:
                    coin -= 1
                    can_play_candidate_card_list[1] -= 1
                    answer += 1
                elif coin > 1 and can_play_candidate_card_list[2] > 0:
                    coin -= 2
                    can_play_candidate_card_list[2] -= 1
                    answer += 1
                else:
                    break
    
    return answer
