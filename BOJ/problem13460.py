import sys
from collections import deque, defaultdict
import heapq

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
board = []
for i in range(N):
	board.append(input())

RED = None
BLUE = None
HOLE = None

roll_vertical = [{} for _ in range(M)]
roll_horizontal = [{} for _ in range(N)]

for i in range(1, N-1):
	prev_j = -1
	for j in range(M):
		if board[i][j] != '#':
			if board[i][j] == "R":
				RED = (i,j)
			elif board[i][j] == "B":
				BLUE = (i, j)
			elif board[i][j] == "O":
				HOLE = (i,j)
			
			if prev_j == -1:
				prev_j = j
		else:
			if prev_j != -1:
				if prev_j != j-1:
					roll_horizontal[i][prev_j] = j - 1
					roll_horizontal[i][j - 1] = prev_j
				prev_j = -1

for j in range(1, M-1):
	prev_i = -1
	for i in range(N):
		if board[i][j] != '#':
			if prev_i == -1:
				prev_i = i
		else:
			if prev_i != -1:
				if prev_i != i-1:
					roll_vertical[j][prev_i] = i-1
					roll_vertical[j][i-1] = prev_i
				prev_i = -1

def chk_hole(prev_i, prev_j, nxt_i, nxt_j):
	if prev_i == nxt_i:
		if HOLE[0] == prev_i:
			if prev_j < nxt_j:
				if prev_j <= HOLE[1] <= nxt_j:
					return True
			else:
				if nxt_j <= HOLE[1] <= prev_j:
					return True
	else:
		if HOLE[1] == prev_j:
			if prev_i < nxt_i:
				if prev_i <= HOLE[0] <= nxt_i:
					return True
			else:
				if nxt_i <= HOLE[0] <= prev_i:
					return True
	return False

LEFT = 0
RIGHT = 1
TOP = 3
BOTTOM = 4
def dfs(red_i, red_j, blue_i, blue_j, direc, num):
	result = 11
	#print(f"red_i : {red_i}, red_j: {red_j}, blue_i : {blue_i}, blue_j : {blue_j}, num : {num}")
	if num < 10:
		nxt_red_left_j, nxt_red_right_j = red_j, red_j
		nxt_blue_left_j, nxt_blue_right_j = blue_j, blue_j
		# left and right
		# red
		for nxt_j in roll_horizontal[red_i]:
			if nxt_j <= red_j <= roll_horizontal[red_i][nxt_j]:
				nxt_red_left_j = nxt_j
				nxt_red_right_j = roll_horizontal[red_i][nxt_j]
				break
		# blue
		for nxt_j in roll_horizontal[blue_i]:
			if nxt_j <= blue_j <= roll_horizontal[blue_i][nxt_j]:
				nxt_blue_left_j = nxt_j
				nxt_blue_right_j = roll_horizontal[blue_i][nxt_j]
				break
		
		if red_i == blue_i:
			if nxt_red_left_j == nxt_blue_left_j:
				if red_j < blue_j:
					nxt_blue_left_j += 1
				else:
					nxt_red_left_j += 1
			if nxt_red_right_j == nxt_blue_right_j:
				if red_j < blue_j:
					nxt_red_right_j -= 1
				else:
					nxt_blue_right_j -= 1
		
		# left
		if nxt_red_left_j != red_j or nxt_blue_left_j != blue_j:
			if abs(direc-LEFT) > 1:
				if not chk_hole(blue_i, blue_j, blue_i, nxt_blue_left_j-1):
					if chk_hole(red_i, red_j, red_i, nxt_red_left_j-1):
						return num+1
					result = min(dfs(red_i, nxt_red_left_j, blue_i, nxt_blue_left_j, LEFT, num+1), result)
		
		# right
		if nxt_red_right_j != red_j or nxt_blue_right_j != blue_j:
			if abs(direc-RIGHT) > 1:
				if not chk_hole(blue_i, blue_j, blue_i, nxt_blue_right_j+1):
					if chk_hole(red_i, red_j, red_i, nxt_red_right_j+1):
						return num+1
					result = min(dfs(red_i, nxt_red_right_j, blue_i, nxt_blue_right_j, RIGHT, num+1), result)

		# top and bottom
		nxt_red_top_i, nxt_red_bottom_i = red_i, red_i
		nxt_blue_top_i, nxt_blue_bottom_i = blue_i, blue_i
		# red
		for nxt_i in roll_vertical[red_j]:
			if nxt_i <= red_i <= roll_vertical[red_j][nxt_i]:
				nxt_red_top_i = nxt_i
				nxt_red_bottom_i = roll_vertical[red_j][nxt_i]
				break
		# blue
		for nxt_i in roll_vertical[blue_j]:
			if nxt_i <= blue_i <= roll_vertical[blue_j][nxt_i]:
				nxt_blue_top_i = nxt_i
				nxt_blue_bottom_i = roll_vertical[blue_j][nxt_i]
				break
		
		if red_j == blue_j:
			if nxt_red_top_i == nxt_blue_top_i:
				if red_i < blue_i:
					nxt_blue_top_i += 1
				else:
					nxt_red_top_i += 1
			if nxt_red_bottom_i == nxt_blue_bottom_i:
				if red_i < blue_i:
					nxt_red_bottom_i -= 1
				else:
					nxt_blue_bottom_i -= 1
		
		#top
		if nxt_red_top_i != red_i or nxt_blue_top_i != blue_i:
			if abs(direc-TOP) > 1:
				if not chk_hole(blue_i, blue_j, nxt_blue_top_i - 1, blue_j):
					if chk_hole(red_i, red_j, nxt_red_top_i - 1, red_j):
						return num+1
					result = min(dfs(nxt_red_top_i, red_j, nxt_blue_top_i, blue_j, TOP, num+1), result)
		
		# bottom
		if nxt_red_bottom_i != red_i or nxt_blue_bottom_i != blue_i:
			if abs(direc-BOTTOM) > 1:
				if not chk_hole(blue_i, blue_j, nxt_blue_bottom_i + 1, blue_j):
					if chk_hole(red_i, red_j, nxt_red_bottom_i + 1, red_j):
						return num+1
					result = min(dfs(nxt_red_bottom_i, red_j, nxt_blue_bottom_i, blue_j, BOTTOM, num+1), result)
		
	return result
		
result = dfs(RED[0], RED[1], BLUE[0], BLUE[1], -2, 0)
if result == 11:
	print(-1)
else:
	print(result)
