import sys

input = lambda:sys.stdin.readline().rstrip()

def str_sum(str1):
    return sum(int(char) for char in str1 if char.isdigit())

N = int(input())

word_list = []
for _ in range(N):
    word_list.append(input())

word_list.sort()
word_list.sort(key=lambda y:str_sum(y))
word_list.sort(key=len)

print('\n'.join(word_list))

# regular expression 사용시 실행시간이 증가함.