#난이도 상에 가까운 문제이다.
#구현 난이도가 어렵다. ->트리의 기본적인 특징이 필요하다.
#중위 순회는 x축을 기준으로 왼쪽부터 방문한다는 특징이 있다.\
#레벨값을 저장해보자.
'''
class Node:
    def __init__(self, number, left_node, right_node):
        self.parent = -1
        self.number = number
        self.left_node = left_node
        self.right_node = right_node

def in_order(node, level):
    global level_depth, x
    level_depth =max(level_depth,level)
    #왼쪽노드 도는 것
    if node.left_node != -1:
        in_order(tree[node.left_node],level+1)
    #데이터 처리하는 곳 : 나중에 데이터 차이 구해 놓을려고 : 너비의 차와 높이의 차를 구하려면 왼쪽 노드를 브랜치를 확인 하는 것이 옳다.
    level_min[level] = min(level_min[level], x)
    level_max[level] = max(level_max[level], x)
    x += 1
    #오른쪽노드 도는 것
    if node.right_node !=-1:
        in_order(tree[node.right_node],level+1)

n=int(input())
tree={}
level_min=[n]
level_max=[0]
root=-1
x=1
level_depth =1


#부모가 없는 놈이 루트라고 가정을하고 순회 시작하면 된다.
for i in range(1,n+1):
    tree[i] = Node(i,-1,-1)
    level_min.append(n)
    level_max.append(0)


for _ in range(n):
    number,left_node,right_node = map(int,input().split())
    tree[number].left_node = left_node
    tree[number].right_node = right_node
    if left_node != -1:
        tree[left_node].parent=number
    if right_node != -1:
        tree[right_node].parent =number

for i in range(1,n+1):
    if tree[i].parent ==-1:
        root = i

in_order(tree[root],1)

result_level = 1
result_width = level_max[1] - level_min[1] + 1
#중요
for i in range(2,level_depth + 1):
    width =level_max[i]-level_min[i]+1
    if result_width < width:
        result_level = i
        result_width = width

print(result_level,result_width)

'''

import sys
input = sys.stdin.readline
from collections import deque


class Node:
    x, y = 0, 0
    lc, rc = 0, 0
    ln, rn = 0, 0
    p = 0



def dfs(i):
    lc, rc = 0, 0
    ln, rn = g[i].ln, g[i].rn
    if ln > 0:
        lc = dfs(ln)
    if rn > 0:
        rc = dfs(rn)

    g[i].lc = lc
    g[i].rc = rc

    return lc + rc + 1


def bfs(i):
    g[i].x, g[i].y = 1, 1 + g[i].lc
    q = deque([i])
    while q:
        k = q.popleft()
        l, r = g[k].ln, g[k].rn
        f[g[k].x].append(g[k].y)

        if l > 0:
            g[l].x = g[k].x + 1
            g[l].y = g[k].y - g[l].rc - 1
            q.append(l)
        if r > 0:
            g[r].x = g[k].x + 1
            g[r].y = g[k].y + g[r].lc + 1
            q.append(r)


def find_root(i):
    if g[i].p == 0:
        return i
    return find_root(g[i].p)


n = int(input())
g = dict([(i, Node()) for i in range(1, n + 1)])
f = [[] for _ in range(50)]
for i in range(n):
    x, y, z = map(int, input().split())
    if y > 0:
        g[x].ln = y
        g[y].p = x
    if z > 0:
        g[x].rn = z
        g[z].p = x


root = find_root(1)
dfs(root)
bfs(root)


mi, mv = 0, 0


for i in range(1, 50):

    if len(f[i]) == 0:
        break
    v = max(f[i]) - min(f[i]) + 1
    if mv < v:
        mv = v
        mi = i


print(mi, mv)