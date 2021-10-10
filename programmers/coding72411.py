from itertools import combinations

def solution(orders, course):
    answer = []
    for menu_num in course:
        sel_course = {}
        for menu_order in orders:
            if len(menu_order) >= menu_num:
                for menu in list(combinations(menu_order, menu_num)):
                    menu = tuple(sorted(menu))
                    if menu in sel_course:
                        sel_course[menu] += 1
                    else:
                        sel_course[menu] = 1
        sorted_menu = sorted(sel_course, key = lambda x: sel_course[x], reverse=True)
        if len(sorted_menu) > 0:
            max_iter_item = sorted_menu[0]
            max_iter = sel_course[max_iter_item]
            i = 1
            if max_iter > 1:
                while( sel_course[max_iter_item] == max_iter ):
                    answer.append(''.join(max_iter_item))
                    if i == len(sorted_menu):
                        break
                    max_iter_item = sorted_menu[i]
                    i += 1
    answer.sort()
    return answer