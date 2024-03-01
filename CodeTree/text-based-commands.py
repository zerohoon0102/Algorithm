cmd = input()

i_dir = [-1, 0, 1, 0]
j_dir = [0, -1, 0, 1]

no_error = [(0,0)]
y, x = 0, 0

direc_info = [0]*len(cmd)
direc = 0

for i in range(len(cmd)):
    c = cmd[i]
    if c == "F":
        y += i_dir[direc]
        x += j_dir[direc]
    elif c == "R":
        direc = (direc+3)%4
    elif c == "L":
        direc = (direc+1)%4
    no_error.append((y, x))
    if i < len(cmd) - 1:
        direc_info[i+1] = direc

last_i, last_j = no_error[-1]
end = set()

for t in range(1, len(cmd)+1):
    c = cmd[t-1]
    after_i, after_j = last_i - no_error[t][0],  last_j - no_error[t][1]
    cur_i, cur_j = no_error[t-1]
    direc = direc_info[t-1]
    if c == "F":
        # R
        end.add(( cur_i - after_j  , cur_j + after_i ))
        # L
        end.add(( cur_i + after_j  , cur_j - after_i ))
    elif c == "R":
        # F
        end.add(( cur_i + i_dir[direc] - after_j  , cur_j + j_dir[direc] + after_i ))
        # L
        end.add(( cur_i - after_i  , cur_j - after_j ))
    elif c == "L":
        # F
        end.add(( cur_i + i_dir[direc] + after_j  , cur_j + j_dir[direc] - after_i ))
        # R
        end.add(( cur_i - after_i  , cur_j - after_j ))

print(len(end))
