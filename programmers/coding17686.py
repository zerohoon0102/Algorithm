def solution(files):
    answer = []
    a = re.compile('\d+')
    tmp_dict = {}
    for filename in files:
        idx = filename.index(a.findall(filename)[0])
        tmp_dict[filename] = filename[0:idx].lower()
    tmp_arr = [k for k, v in sorted(tmp_dict.items(), key=lambda x: x[1])]
    tmp = {}
    for filename in tmp_arr:
        if len(tmp) == 0:
            tmp[filename] = int(a.findall(filename)[0])
        else:
            for name in tmp:
                if tmp_dict[name] == tmp_dict[filename]:
                    tmp[filename] = int(a.findall(filename)[0])
                else:
                    answer.extend([k for k, v in sorted(tmp.items(), key=lambda x: x[1])])
                    tmp.clear()
                    tmp[filename] = int(a.findall(filename)[0])
                break
    if len(tmp) != 0:
        answer.extend([k for k, v in sorted(tmp.items(), key=lambda x: x[1])])
    return answer


import re