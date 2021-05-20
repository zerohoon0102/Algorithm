def solution(gems):
    answer = [-1,100002]
    kind_num = len(set(gems))
    gem_cnt = {}
    left = 0
    right = 0
    while(right < len(gems)):
        if gems[right] in gem_cnt:
            gem_cnt[gems[right]] += 1
        else:
            gem_cnt[gems[right]] = 1
        right += 1
        if len(gem_cnt) == kind_num:
            while(gem_cnt[gems[left]] > 1):
                gem_cnt[gems[left]] -= 1
                left += 1
            if (answer[1]-answer[0]) > (right - left - 1):
                answer = [left + 1, right]
    return answer