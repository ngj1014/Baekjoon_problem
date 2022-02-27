import sys
input=sys.stdin.readline

#row, col순서임
h,w=map(int, input().split())
lst=list(map(int, input().split()))


height=h
count=0
start , end = 0 , 0
dap=0
while True:
    if height==0:
        break
    for i in range(w):
        if count == 0 and height <= lst[i]:
            start = i
            count += 1
        elif count > 0 and height <= lst[i]:
            end = i
            count = 0
            dap += (end - start-1)
            start=i
            count+=1

    height-=1
    count=0



print(dap)



