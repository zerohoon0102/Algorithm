def test_perfect(u):
    left_num = len(u)/2
    right_num = left_num
    for a in range(0, len(u)):
        if u[a] == '(':
            left_num = left_num - 1
        else:
            right_num = right_num - 1
        if left_num > right_num:
            return False
    return True

def test_uniform(p):
    left_num = 1
    for a in range(0, len(p)):
        if p[a] == '(':
            left_num = left_num + 1
        else:
            left_num = left_num - 1
    if left_num == 1:
        return True
    else:
        return False

def to_perfect(p):
    u = ""
    v = ""
    start = 0
    end = 2
    while u == "":
        if test_uniform(p[start:end]):
            u = p[start:end]
            v = p[end:len(p)]
        else:
            end = end + 2
    print(u)
    print(v)
    if test_perfect(u):
        if v == "":
            return u
        else:
            return u + to_perfect(v)
    else:
        if v == "":
            for u_in in range(1, len(u)-1):
                if u[u_in] == '(':
                    u = u[0:u_in] + ')' + u[u_in + 1:len(u)]
                else:
                    u = u[0:u_in] + '(' + u[u_in + 1:len(u)]
            return "()" + u[1:len(u)-1]
        else:
            for u_in in range(1, len(u)-1):
                if u[u_in] == '(':
                    u = u[0:u_in] + ')' + u[u_in + 1:len(u)]
                else:
                    u = u[0:u_in] + '(' + u[u_in + 1:len(u)]
            return '(' + to_perfect(v) + ')' + u[1:len(u)-1]

def solution(p):
    if p == "":
        return ""
    else:
        if test_perfect(p):
            return p
        else:
            return to_perfect(p)