def solution(record):
    split_record = [re.split() for re in record]
    uid_name = {}
    for a in split_record:
        if a[0][0] != "L":
            uid_name[a[1]] = a[2]
    
    answer = []
    for n in split_record:
        if n[0][0] == "E":
            answer.append(uid_name[n[1]] + '님이 들어왔습니다.')
        elif n[0][0] == "L":
            answer.append(uid_name[n[1]] + '님이 나갔습니다.')
    return answer