import sys
input = sys.stdin.readline

n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

dap=0

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            flag = False
            if i == j or i == k or j == k:
                continue
            else:
                for l in range(n):
                    strike, ball = 0, 0
                    if str(lst[l][0])[0] == str(i):
                        strike+=1
                    elif str(i) in str(lst[l][0]):
                        ball+=1
                    if str(lst[l][0])[1] == str(j):
                        strike+=1
                    elif str(j) in str(lst[l][0]):
                        ball+=1
                    if str(lst[l][0])[2] == str(k):
                        strike+=1
                    elif str(k) in str(lst[l][0]):
                        ball+=1


                    if lst[l][1] != strike or lst[l][2] != ball:
                        flag = True

                    if flag == True:
                        break

                    if flag == False and l == n-1:
                        dap+=1

print(dap)