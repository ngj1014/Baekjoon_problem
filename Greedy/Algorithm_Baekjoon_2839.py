#백준 설탕
n = int(input())
count=0
q = n // 5
r = n % 5
while True:
    if (r%3)==0:
        count = int(q+(r/3))
        break
    else:
        q-=1
        r=r+5
        if q<0:
            count=-1
            break


print(count)
