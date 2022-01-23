m=input()
count=0 #모든 원소 0으로 만듬
count_2=0 #모든 원소 1으로 만듬

for i in range(len(m)-1):
    if m[0]=='1':
        count+=1
    elif m[i]=='0'and m[i+1]=='1':
        count+=1


for i in range(len(m)-1):
    if m[0]=='0':
        count_2+=1
    elif m[i]=='1'and m[i+1]=='0':
        count_2+=1

print(min(count,count_2))


