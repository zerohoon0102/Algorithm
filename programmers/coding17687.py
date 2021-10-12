def covt2n(num, nth):
	q, r = divmod(num, nth)
	n = '0123456789ABCDEF'[r]
	return covt2n(q, nth) + n if q else n

def solution(n, t, m, p):
    answer = ''
    tmp = ''
    num = 0
    while len(tmp) < m*(t-1) + p:
        tmp += covt2n(num, n)
        num += 1
    num = p - 1
    print(tmp)
    while len(answer) < t:
        answer += tmp[num]
        num += m
    return answer