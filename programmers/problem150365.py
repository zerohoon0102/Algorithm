def solution(n, m, x, y, r, c, k):
    answer = ''
    width, height = c-y, r-x
    ver = [1, 0, 0, -1]
    hor = [0, -1, 1, 0]
    direc_c = ['d', 'l', 'r', 'u']
    if k < abs(width)+abs(height) or (k-abs(width)-abs(height))%2 == 1:
        answer = "impossible"
    else:
        cur_x, cur_y = x, y
        while k:
            for i in range(4):
                if 0 < cur_x+ver[i] <= n and 0 < cur_y+hor[i] <= m:
                    if abs(height-ver[i])+abs(width-hor[i]) < k:
                        cur_x += ver[i]
                        cur_y += hor[i]
                        k -= 1
                        height -= ver[i]
                        width -= hor[i]
                        answer += direc_c[i]
                        break
    return answer