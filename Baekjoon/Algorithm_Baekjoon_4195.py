#시간 길게 풀음-> 1번풀이
"""
def networknum(arr, n):
    check=[]
    global dap
    dap=2
    global chuga
    chuga=0
    for _ in range(n):
        x,y=input().split(' ')
        check.append(x)
        check.append(y)

        for i in range(len(check)-2):
            if len(check)==2:
                break;
            else:
                for j in range(len(check)-2,len(check)):
                    if check[i]==check[j]:
                        dap+=1
                        break
        print(dap)




lst = []
for _ in range(int(input())):
    # f는 인간 관계의 수
    f = int(input())
    networknum(lst, f)
"""
#2번 union-find함수 이용하기
# 집합이용해서  Union_find함수를 이용할 예정->합집합 찾기.-> 연결여부 찾는 알고리즘.
# in , not in 함수 이용하면 존재여부를 쉽게 판단 할수 있다.
# 해쉬 문제는 집합을 이용하면 편하다.

def find(x):
    if x==parent[x]:
        return x
    else:
        p=find(parent[x])
        parent[x]=p
        return parent[x]

def union(x, y):
    x=find(x)
    y=find(y)

    if x!=y:
        parent[y]=x
        number[x]+=number[y]


test_case=int(input())
for _ in range(test_case):
    parent=dict()
    number=dict()

    f=int(input())

    for _ in range(f):
        x,y=input().split(' ')

        if x not in parent:
            parent[x]=x
            number[x]=1
        if y not in parent:
            parent[y]=y
            number[y]=1

        union(x,y)
        print(number[find(x)])