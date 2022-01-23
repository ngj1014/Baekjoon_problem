n=int(input())
lst=input()
result=0
bonus=0
for i in range(n):
    if lst[i]=='X':
        bonus=0
    else:
        result+=bonus
        result+=(i+1)
        bonus+=1

print(result)