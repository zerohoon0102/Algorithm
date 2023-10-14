discount = [10, 20, 30, 40]
def solution(users, emoticons):
    answer = [0,0]
    
    def dfs(idx, buyers, answer):
        emoticon = emoticons[idx]
        for dis in discount:
            for i in range(len(buyers)):
                if users[i][0] <= dis:
                    buyers[i] += (emoticon//100)*(100-dis)
            if idx == len(emoticons)-1:
                cur_result = [0,0]
                for i in range(len(buyers)):
                    if buyers[i] >= users[i][1]:
                        cur_result[0] += 1
                    else:
                        cur_result[1] += buyers[i]
                
                if cur_result[0] > answer[0]:
                    answer[0] = cur_result[0]
                    answer[1] = cur_result[1]
                elif cur_result[0] == answer[0]:
                    if cur_result[1] > answer[1]:
                        answer[1] = cur_result[1]
            else:
                dfs(idx+1, buyers, answer)
            for i in range(len(buyers)):
                if users[i][0] <= dis:
                    buyers[i] -= (emoticon//100)*(100-dis)
    dfs(0, [0]*len(users), answer)
    return answer
