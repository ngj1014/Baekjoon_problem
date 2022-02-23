'''완전 탐색으로 했는데 안됨.
n = int(input())

lst=list(map(int , input().split()))

lst.sort()

lst_positive=[]
lst_negative=[]
dap=[]

for i in range(len(lst)):
    if lst[i]<0:
        lst_negative.append(lst[i])
    else:
        lst_positive.append(lst[i])

lst_negative.sort(reverse=True)

count_positive=0
count_negative=0
leng_negative=len(lst_negative)
leng_positive=len(lst_positive)

if abs(lst_negative[count_negative])<abs(lst_positive[count_positive]):
    dap.append(lst_negative[0])
    count_negative+=1
    leng_negative-=1
    lst_negative.remove(lst_negative[0])
elif abs(lst_negative[count_negative])>abs(lst_positive[count_positive]):
    dap.append(lst_positive[0])
    count_positive+=1
    leng_positive-=1
    lst_positive.remove(lst_positive[0])
else:
    dap.append(lst_negative[0])
    dap.append(lst_positive[0])
    count_negative+=1
    count_positive+=1
    if abs(lst_negative[count_negative])<abs[lst_positive[count_positive]]:
        dap.append(lst_negative[count_negative])
        dap.sort()
        print(dap)
        exit(0)
    else:
        dap.append(lst_positive[count_positive])
        dap.sort()
        print(dap)
        exit(0)

mini=1e9
result=dap
count=0
lst_2=lst_negative+lst_positive
for i in range(len(lst_2)-1):
    for j in range(i+1,len(lst_2)):
        if count==0:
            if mini > abs(lst_2[i]+lst_2[j]+dap[0]):
                result.append(lst_2[i])
                result.append(lst_2[j])
                count=1
                mini=abs(sum(result))
        else:
            if mini>abs(lst_2[i]+lst_2[j]+dap[0]):
                result.remove(result[2])
                result.remove(result[1])
                result.append(lst_2[i])
                result.append(lst_2[j])
                mini=abs(sum(result))

result.sort()
print(result)
'''

import sys
input= sys.stdin.readline

n=int(input())

lst=list(map(int, input().split()))
lst.sort()

maximum=4000000000
sol_lst=[]

#fix 한 것이다.
for i in range(n-2):
    fix=lst[i]
    #fix바로 오른쪽(왼쪽에서 출발한다는 뜻.)
    left=i+1
    #오른쪽에서 출발한다는 뜻.
    right=n-1

    while left<right:
        cur_sum=fix+lst[left]+lst[right]

        if abs(cur_sum)<=abs(maximum):
            sol_lst=[fix,lst[left],lst[right]]
            maximum=fix+lst[left]+lst[right]

        if cur_sum<0:
            left+=1
        elif cur_sum>0:
            right-=1
        #합 0이면 끝내야함 무조건 최소값임.
        else:
            #리스트 형식말고 값을 출력하는 방법
            print(*sol_lst)
            sys.exit()

#리스트 형식말고 값을 출력하는 방법
print(*sol_lst)

