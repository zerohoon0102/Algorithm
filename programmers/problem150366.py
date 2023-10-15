def find_root_cell(r, c, merged, table):
    if merged[r][c]:
        nxt_r, nxt_c = table[r][c]
        table[r][c] = find_root_cell(nxt_r, nxt_c, merged, table)
        return table[r][c]
    else:
        return (r, c)

def solution(commands):
    answer = []
    table = [[""]*51 for _ in range(51)]
    idx_group = [[set([(i,j)]) for j in range(51)] for i in range(51)]
    merged = [[False]*51 for _ in range(51)]
    value_arr = {}
    
    for command in commands:
        command = command.split()
        if command[0] == "UPDATE":
            if len(command) == 4:
                r, c, value = command[1:]
                r, c = find_root_cell(int(r), int(c), merged, table)
                
                table[r][c] = value
                if value not in value_arr:
                    value_arr[value] = set()
                value_arr[value].add((r,c))
            else:
                value1, value2 = command[1:]
                if value1 == value2:
                    continue
                if value1 not in value_arr:
                    continue
                if value2 not in value_arr:
                    value_arr[value2] = set()
                for r, c in value_arr[value1]:
                    if table[r][c] != value1:
                        continue
                    table[r][c] = value2
                    value_arr[value2].add((r,c))
                del value_arr[value1]
        elif command[0] == "MERGE":
            r1, c1, r2, c2 = map(int, command[1:])
            r1, c1 = find_root_cell(r1, c1, merged, table)
            r2, c2 = find_root_cell(r2, c2, merged, table)
            if r1 == r2 and c1 == c2:
                continue
            
            if not table[r1][c1] and table[r2][c2]:
                table[r1][c1] = (r2, c2)
                idx_group[r2][c2].update(idx_group[r1][c1])
                idx_group[r1][c1].clear()
                merged[r1][c1] = True
            else:
                table[r2][c2] = (r1, c1)
                idx_group[r1][c1].update(idx_group[r2][c2])
                idx_group[r2][c2].clear()
                merged[r2][c2] = True
        elif command[0] == "UNMERGE":
            r, c = map(int, command[1:])
            target_r, target_c = r, c
            r, c = find_root_cell(r, c, merged, table)
            
            value = table[r][c]
            for nxt_r, nxt_c in idx_group[r][c]:
                table[nxt_r][nxt_c] = ""
                merged[nxt_r][nxt_c] = False
                if r == nxt_r and c == nxt_c:
                    continue
                idx_group[nxt_r][nxt_c] = set([(nxt_r,nxt_c)])
            idx_group[r][c] = set([(r, c)])
            table[target_r][target_c] = value
            if value:
                value_arr[value].add((target_r, target_c))
        elif command[0] == "PRINT":
            r, c = map(int, command[1:])
            r, c = find_root_cell(r, c, merged, table)
            if not table[r][c]:
                answer.append("EMPTY")
            else:
                answer.append(table[r][c])
    return answer
