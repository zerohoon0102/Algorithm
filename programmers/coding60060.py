from collections import defaultdict
def solution(words, queries):
    answer = [0]*len(queries)
    
    word_info_front = {}
    word_info_back = {}
    chk_num = [0]*10001
    for word in words:
        length = len(word)
        chk_num[length] += 1
        if length not in word_info_front:
            word_info_front[length] = {}
            word_info_back[length] = {}
        cur_front = word_info_front[length]
        for i in range(length):
            s = word[i]
            if s in cur_front:
                cur_front[s][0] += 1
                cur_front = cur_front[s]
            else:
                cur_front[s] = {0: 1}
                cur_front = cur_front[s]
        
        cur_back = word_info_back[length]
        for i in range(length-1, -1, -1):
            s = word[i]
            if s in cur_back:
                cur_back[s][0] += 1
                cur_back = cur_back[s]
            else:
                cur_back[s] = {0: 1}
                cur_back = cur_back[s]
    
    for i, query in enumerate(queries):
        length = len(query)
        if chk_num[length]:
            if query[-1] == '?':
                cur_front = word_info_front[length]
                if query[0] == '?':
                    answer[i] = chk_num[length]
                    continue
                for s in query:
                    if s == '?':
                        answer[i] = cur_front[0]
                        break
                    else:
                        if s in cur_front:
                            cur_front = cur_front[s]
                        else:
                            break
            else:
                cur_back = word_info_back[length]
                for s in query[::-1]:
                    if s == '?':
                        answer[i] = cur_back[0]
                        break
                    else:
                        if s in cur_back:
                            cur_back = cur_back[s]
                        else:
                            break
    
    return answer