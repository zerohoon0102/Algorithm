def solution(expression):
    answer = 0
    e = expression
    arr = re.findall('\d+|\-|\*|\+', e)
    reset_arr = arr.copy()
    exp = []
    if '-' in arr:
        exp.append('-')
    if '+' in arr:
        exp.append('+')
    if '*' in arr:
        exp.append('*')
    exp = list(permutations(exp, len(exp)))
    for tmp_exp in exp:
        for n in range(len(tmp_exp)):
            while tmp_exp[n] in arr:
                idx = arr.index(tmp_exp[n])
                tmp = eval(arr[idx-1]+arr[idx]+arr[idx+1])
                tmp = str(tmp)
                del arr[idx-1:idx+2]
                arr.insert(idx-1, tmp)
        if abs(int(arr[0])) > answer:
            answer = abs(int(arr[0]))
        arr = reset_arr.copy()
    return answer

import re
from itertools import permutations