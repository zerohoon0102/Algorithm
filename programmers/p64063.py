import sys
# recursion이 n=200,000까지 일어날 수 있음
sys.setrecursionlimit(200001)
def find_and_update_nxt_room(room_info: dict, room: int):
    if room not in room_info:
        return room
    room_info[room] = find_and_update_nxt_room(room_info, room_info[room])
    return room_info[room]

def solution(k, room_number):
    answer = []
    room_info = {}
    for room in room_number:
        # room이 room_info에 없는 경우 아직 이용되지 않은 것임.
        # room이 없는 경우 room+1이 가르키는 곳을 가르키게 하는 방식으로 진행.
        if room not in room_info:
            assigned_room = room
            room_info[room] = find_and_update_nxt_room(room_info, room+1)
        else:
            assigned_room = find_and_update_nxt_room(room_info, room_info[room])
            room_info[assigned_room] = find_and_update_nxt_room(room_info, assigned_room+1)
            room_info[room] = room_info[assigned_room]
        answer.append(assigned_room)
    return answer
