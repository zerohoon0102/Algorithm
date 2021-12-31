import sys
import re


def make_exp(val):
    result = ''
    chk = False
    queue = []
    group = 0
    left = ''
    right = ''
    for i,c in enumerate(val):
        if 'A' <= c <= 'Z':
            
        else:
            if c == "*" or c == "/":
                
            elif c == "+" or c == "-":
                
            elif c == "(":
                group = True
            elif c == ")" and i == len(val)-1:
                result += ')'
            result += c
    
    result = "(" + result + ")"
    return result

def make_post(val):
    stack = []
    result = ''
    for c in val:
        if 'A' <= c <= 'Z':
            result += c
        else:
            if c == ')':
                t = stack.pop()
                if t != "(":
                    result += t
                    stack.pop()
            else:
                stack.append(c)
    print(stack)
    while stack:
        result += stack.pop()
    return result

exp = sys.stdin.readline().rstrip()
exp = make_exp(exp)
print(exp)
exp = make_post(exp)
print(exp)
