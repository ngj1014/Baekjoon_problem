#전위 순회: (본인) -> 왼쪽자식 -> 오른쪽자식 순서
#중위 순회: 왼쪽자식 -> (본인) -> 오른쪽자식 순서
#후위 순회: 왼쪽자식 -> 오른쪽자식 ->  (본인) 순서
#트리 노드의 수 ex) n=7 -> 노드 A,B,C,D,E,F,G

import sys
input = sys.stdin.readline

n = int(input())
tree = {}
for i in range(n):
    root, left, right = list(input().split())
    tree[root] = [left, right]

# 전위 순회 root -> left -> right
def preorder(tree, root): # 트리와 시작점이 될 루트를 받아야한다.
    preorder_result.append(root)
    if tree[root][0] != '.' or None:
        preorder(tree, tree[root][0])
    if tree[root][1] != '.' or None:
        preorder(tree, tree[root][1])
    return preorder_result

# 중위 순회 left -> root -> right
def inorder(tree, root):
    if tree[root][0] != '.' or None:
        inorder(tree, tree[root][0])
    inorder_result.append(root)
    if tree[root][1] != '.' or None:
        inorder(tree, tree[root][1])
    return inorder_result

# 후위 순위 right -> root -> left
def postorder(tree, root):
    if tree[root][0] != '.' or None:
        postorder(tree, tree[root][0])
    if tree[root][1] != '.' or None:
        postorder(tree, tree[root][1])
    postorder_result.append(root)
    return postorder_result

preorder_result = []
print(''.join(preorder(tree, 'A')))
inorder_result = []
print(''.join(inorder(tree, 'A')))
postorder_result = []
print(''.join(postorder(tree, 'A')))

