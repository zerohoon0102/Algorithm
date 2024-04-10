def solution(board, skill):
    answer = 0
    N, M = len(board), len(board[0])
    # skill에 대한 정보를 담기 위한 리스트 선언
    skill_info = [[0]*M for _ in range(N)]
    
    # prefix_sum을 통해 결과를 업데이트할 때, prefix_sum에 스킬 결과를 반영하기 위한 업데이트
    # 왼쪽 위에서 값을 추가하고, 열이나 행에서 벗어나면 해당 값을 뺄 수 있도록 업데이트
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            degree = -degree
        skill_info[r1][c1] += degree
        if r2+1 < N:
            skill_info[r2+1][c1] -= degree
            if c2+1 < M:
                skill_info[r2+1][c2+1] += degree
        if c2+1 < M:
            skill_info[r1][c2+1] -= degree
    
    # 현재 열을 이전 열의 결과를 기반으로 사용하면, 위에서 skill_info에 skill영역의 네 꼭지점에만 값을 적용하는 것을 이용할 수 있음.
    # 맨 윗 열에서 prefix sum을 통해 반영이 되었다면, 이전 열을 이번열의 기반으로 사용하면 skill을 적용한 것처럼 이용 가능.
    cur_arr = [0]*M
    for i in range(N):
        prefix_sum = 0
        for j in range(M):
            prefix_sum += skill_info[i][j]
            cur_arr[j] += prefix_sum
            if cur_arr[j] + board[i][j] > 0:
                answer += 1
    
    return answer
