'''시간 초과 뜸 완전 탐색으로 품.
n, k = map(int, input().split())

lst = []

a = n+1
b = n*2
lst.append(a)
lst.append(b)

d=b-a-2
new=b
while d>0:
    new=b+d
    lst.append(new)
    d-=2


if k in lst:
    print("YES")
else:
    print("NO")
'''
#입력값때문에 이진탐색을 생각함.
n, k=map(int,input().split())
left=0
#대칭성 때문에 끝까지 체크할 필요가 없다. -> 근데 n으로 계산해도 충분히 계산됨을 확인함.
#right=n//2
#덜헷갈림.
right=n

while left<=right:
    rowcut=(left+right)//2
    colcut=n-rowcut
    #제일중요함.
    pieces=(rowcut+1)*(colcut+1)
    if k == pieces:
        print("YES")
        exit(0)
    elif k>pieces:
        left=rowcut+1
    else:
        right=rowcut-1

print("NO")