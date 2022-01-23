n=0
mylist = list(map(int, input().split()))
"""1번
for i in range(8):
    if mylist[i] == i+1:
        n+=1
    elif mylist[i] == (8-i):
        n-=1


if n==8:
    print("ascending")
elif n==(-8):
    print("descending")
else:
    print("mixed")
"""
"""2번풀이"""
ascending=True
descending=True

for i in range(1,8):
    if mylist[i]>mylist[i-1]:
        descending=False
    elif mylist[i]<mylist[i-1]:
        ascending=False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")