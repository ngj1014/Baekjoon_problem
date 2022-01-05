n,m=list(map(int,input().split()))
lst,lst_2=input().split()
alp=[3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
num=min(n,m)
num_2=max(n,m)
num_3=num_2-num
lst_arr=''
for i in range(num):
    lst_arr+=lst[i]+lst_2[i]

lst_arr+=lst[num:]+lst_2[num:]

result=[alp[ord(i)-ord('A')] for i in lst_arr]

for i in range(n+m-2):
    for j in range(n+m-1-i):
        result[j]+=result[j+1]

print("{}%".format(result[0]%10*10+result[1]%10))