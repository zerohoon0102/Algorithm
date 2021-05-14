from collections import deque

def solution(enroll, referral, seller, amount):
    answer = []
    money = {}
    parent = {}
    for idx in range(len(enroll)):
        parent[enroll[idx]] = referral[idx]
        money[enroll[idx]] = 0
    for i in range(len(seller)):
        queue = deque([seller[i]])
        rest = amount[i]*100
        while(1):
            cur = queue.popleft()
            if (cur == "-"):
                break
            money[cur] += rest
            if rest < 10:
                break
            rest = rest//10
            money[cur] -= rest
            queue.append(parent[cur])
    for name in enroll:
        answer.append(money[name])
    return answer