def test_alpha(str1):
    if (ord(str1) >= 65 and ord(str1) <= 90) or (ord(str1) >= 97 and ord(str1) <= 122):
        return True
    else:
        return False

def solution(str1, str2):
    if str1 == [] and str2 == []:
        return 65536
    str1_arr = []
    str2_arr = []
    src1 = 0
    src2 = 0
    while src1 < len(str1) - 1:
        if test_alpha(str1[src1]):
            if test_alpha(str1[src1 + 1]):
                str1_arr.append(str1[src1:src1+2].upper())
                src1 = src1 + 1
            else :
                src1 = src1 + 2
        else:
            src1 = src1 + 1
    
    while src2 < len(str2) - 1:
        if test_alpha(str2[src2]):
            if test_alpha(str2[src2 + 1]):
                str2_arr.append(str2[src2:src2 + 2].upper())
                src2 = src2 + 1
            else :
                src2 = src2 + 2
        else:
            src2 = src2 + 1
    same_num = 0
    str1_arr.sort()
    str2_arr.sort()
    b = ""
    for a in str1_arr:
        if a != b:
            temp = 0
            temp = min(str1_arr.count(a), str2_arr.count(a))
            same_num = same_num + temp
        b = a
    
    if str1_arr == [] and str2_arr == []:
        return 65536
    print(len(str1_arr), len(str2_arr), same_num)
    final = len(str1_arr) + len(str2_arr) - same_num
    final = same_num / final
    answer = int(final * 65536)
    return answer