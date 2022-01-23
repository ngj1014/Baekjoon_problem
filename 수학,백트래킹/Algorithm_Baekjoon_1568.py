n=int(input())

count=0
k=1
while True:
    if n==0:
        break
    if n-k<0:
        k=1
    n=n-k
    count+=1
    k+=1


print(count)