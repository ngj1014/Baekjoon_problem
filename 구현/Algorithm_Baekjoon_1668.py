'''
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
'''

#제 2풀이 ascending
def ascending(array):
    now=array[0]
    result=1
    for i in range(1,len(array)):
        if now < array[i]:
            result+=1
            now = array[i]

    return result

n=int(input())
array=[]

for _ in range(n):
    array.append(int(input()))

print(ascending(array))
array.reverse()
print(ascending(array))