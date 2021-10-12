def changeStr(s) :
    s = s.replace('A#','a')
    s = s.replace('F#','f')
    s = s.replace('C#','c')
    s = s.replace('D#','d')
    s = s.replace('G#','g')
    return s

def solution(m, musicinfos):
    m = changeStr(m)
    answer = ''
    song_info_list = []
    for song in musicinfos:
        temp_info = song.split(',')
        temp_str = changeStr(temp_info[3])
        temp_bef_time = temp_info[0].split(':')
        temp_aft_time = temp_info[1].split(':')
        dif_time = 60*(int(temp_aft_time[0]) - int(temp_bef_time[0])) + int(temp_aft_time[1]) - int(temp_bef_time[1])
        temp_str = temp_str * (dif_time // len(temp_str)) + temp_str[0:(dif_time % len(temp_str))]
        song_info_list.append([f"{temp_info[2]}", f"{temp_str}"])
    length = len(song_info_list)
    answer = "(None)"
    print(song_info_list)
    idx = 0
    chk_answer = ""
    while idx < length:
        if song_info_list[idx][1].find(m) == -1:
            del song_info_list[idx]
            length -= 1
            idx -= 1
        else:
            if (len(chk_answer) < len(song_info_list[idx][1])) or (answer == "(None)"):
                answer = song_info_list[idx][0]
                chk_answer = song_info_list[idx][1]
        idx += 1
    return answer