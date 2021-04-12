score = {'H': 1, 'C': 12, 'O': 16}

chemi = input()

i = 0

def calculate():
    global i
    total = 0
    while(1):
        if i == len(chemi):
            break
        if chemi[i] == '(':
            i += 1
            total += calculate()
        elif chemi[i] == ')':
            i += 1
            if i < len(chemi):
                if chemi[i].isdigit():
                    total *= int(chemi[i])
                    i += 1
            return total
        elif chemi[i].isdigit() == False:
            tmp = score[chemi[i]]
            i += 1
            total += tmp
            if i < len(chemi):
                if chemi[i].isdigit():
                    total += tmp*(int(chemi[i]) - 1)
                    i += 1
    return total
            



print(calculate())
