n,m=map(int ,input().split())

lst=[]
name=[]
num=[]

for _ in range(n):
    name = input()
    num = int(input())
    for j in range(num):
        lst.append(input())

print(lst)