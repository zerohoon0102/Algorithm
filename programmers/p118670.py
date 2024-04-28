from collections import deque

def rotate(left, right, top, bottom):
    # 왼쪽 위 모서리
    lt = left.popleft()
    top.appendleft(lt)
    # 오른쪽 위 모서리
    tr = top.pop()
    right.appendleft(tr)
    # 오른쪽 아래 모서리
    rb = right.pop()
    bottom.append(rb)
    # 왼쪽 아래 모서리
    bl = bottom.popleft()
    left.append(bl)

def shift_row(left, right, center):
    # 왼쪽 라인 교체
    left.appendleft(left.pop())
    # 오른쪽 라인 교체
    right.appendleft(right.pop())
    # 가운데 교체
    center.appendleft(center.pop())

# Rotate는 모서리를 어떻게 효율적으로 처리하냐가 중요하고
# ShiftRow는 맨 윗줄을 어떻게 효율적으로 아래에 붙이냐가 중요함.
# ShiftRow의 경우 Row Array를 담은 Array를 queue로 선언하면 쉽게 처리가 가능함.
# Rotate의 모서리는 left, right column과 top bottom row를 queue로 선언하여 관리하면 쉽게 처리가 가능함.
# 2개의 조건의 queue를 만족할 수 있도록 맨 왼쪽 column과 오른쪽 column 그리고 가운데 column들을 분리하여 관리함으로써
# 2차원 queue처럼 이용하여 시간복잡도를 최적화함.
def solution(rc, operations):
    answer = []
    center = deque([])
    left, right = deque([]), deque([])
    for idx, row in enumerate(rc):
        left.append(row[0])
        right.append(row[-1])
        center.append(deque(row[1:len(row)-1]))
    
    for operation in operations:
        if operation ==  "Rotate":
            rotate(left=left, right=right, top=center[0], bottom=center[-1])
        elif operation == "ShiftRow":
            shift_row(left=left, right=right, center=center)
    
    for i in range(len(rc)):
        arr = []
        arr.append(left[i])
        for v in center[i]:
            arr.append(v)
        arr.append(right[i])
        answer.append(arr)
    return answer
