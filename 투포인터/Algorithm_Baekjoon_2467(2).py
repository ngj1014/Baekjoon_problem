import sys
input = sys.stdin.readline

n = int(input())
lst = sorted(list(map(int, input().split())))

maximum=2000000000
left=0
right=n-1
dap=[]

while left<right:
    if abs(maximum) >= abs(lst[left]+lst[right]):
        maximum=(lst[left]+lst[right])
        dap=[lst[left],lst[right]]

    if lst[left]+lst[right]>0:
        right-=1
    elif lst[left]+lst[right]<0:
        left+=1
    else:
        print(lst[left], lst[right])
        sys.exit()

for i in range(2):
    print(dap[i],end=" ")
