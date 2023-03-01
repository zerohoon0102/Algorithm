def chk(bit):
    if len(bit) > 1:
        length = len(bit)
        if bit[length//2] == '0':
            if int(bit) == 0:
                return True
            else:
                return False
        else:
            return chk(bit[:length//2]) and chk(bit[length//2 + 1:])
    return True
def solution(numbers):
    answer = []
    for number in numbers:
        string = ''
        while number > 0:
            if number%2 > 0:
                string = '1' + string
            else:
                string = '0' + string
            number //= 2
        rest = 0
        while (len(string) / 2**rest) >= 1:
            rest += 1
        string = '0'*(2**rest - len(string) - 1) + string
        result = chk(string)
        
        if result:
            answer.append(1)
        else:
            answer.append(0)
    return answer