import sys
from collections import defaultdict
input = sys.stdin.readline

#중요하다.
trees = defaultdict(int)
n=0
while True:
    tree = input().rstrip()
    if not tree:
        break
    trees[tree] += 1
    n+=1

trees_lst = list(trees.keys())
trees_lst.sort()

for tree in trees_lst:
    print('%s %.4f' %(tree, trees[tree]/n*100))