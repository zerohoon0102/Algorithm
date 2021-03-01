import sys

number = int(sys.stdin.readline().rstrip())
word_list = {}
set_num = number
while(set_num > 0):
    tmp_input = sys.stdin.readline().rstrip()
    length = len(tmp_input)
    if length not in word_list.keys():
        word_list[length] = [tmp_input]
    elif tmp_input not in word_list[length]:
        word_list[length].append(tmp_input)
    set_num -= 1
for idx in sorted(word_list):
    for src in sorted(word_list[idx]):
        print(src)
