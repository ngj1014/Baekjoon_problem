n,m = map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(list(map(str,input())))

cnt, hap = 0, 0
result = ''

for i in range(m):
    a,c,g,t = 0,0,0,0
    for j in range(n):
        if lst[j][i] == 'T':
            t+=1
        elif lst[j][i] == 'A':
            a+=1
        elif lst[j][i] == 'G':
            g+=1
        elif lst[j][i] == 'C':
            c+=1

    if max(a,c,g,t) == a:
        result += 'A'
        hap += (c+g+t)
    elif max(a,c,g,t) == c:
        result += 'C'
        hap += (a+g+t)
    elif max(a,c,g,t) == g:
        result += 'G'
        hap += (a+c+t)
    elif max(a,c,g,t) == t:
        result += 'T'
        hap += (a+c+g)

print(result)
print(hap)

