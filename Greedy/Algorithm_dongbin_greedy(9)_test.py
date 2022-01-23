'''볼링공 고르기'''
n, m = map(int, input().split())
mylist=list(map(int, input().split()))
mylist.sort()
count=0
for i in range(n):
    for j in range(i+1,n):
        if mylist[i]!=mylist[j]:
            count+=1

print(count)
