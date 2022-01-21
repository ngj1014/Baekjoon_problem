n=int(input())
lst=[]
count=1
count_2=1
for _ in range(n):
    lst.append(int(input()))

for i in range(1,n):
    for j in range(0,i):
        if lst[i]>lst[j]:
            if j == i-1:
                count+=1
        else:
            break

print(count)

lst_2=[]
for i in range(n):
    lst_2.append(lst[n-1-i])

for i in range(1,n):
    for j in range(0,i):
        if lst_2[i]>lst_2[j]:
            if j == i-1:
                count_2 += 1
        else:
            break

print(count_2)