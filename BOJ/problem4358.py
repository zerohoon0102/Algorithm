import sys
input = sys.stdin.readline

trees = {}
total = 0
while 1:
    tree = input().rstrip()
    if tree == "":
        break
    total += 1
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1

for k in sorted(trees):
    print("%s %.4f" % (k,(trees[k]/total)*100))
