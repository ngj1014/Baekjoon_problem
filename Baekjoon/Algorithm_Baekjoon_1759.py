#첫번째풀이
#from itertools import combinations
#L,C=map(int,input().split(' '))
#lst=input().split(' ')
#lst=sorted(lst)
#result=list(combinations(lst,L))
#a,b=0,0
#for i in result:
#    for j in i:
#        if j == "a" or j== "e" or j == "i" or j == "o" or j == "u":
#            a+=1


#    if a>=1 and a<=L-2:
#        print(''.join(i))

#    a=0
#    b=0

#두번째 풀이
def sol(a, b, p, d):

    if len(d) == l:
        if a > 0 and b > 1:
            print(d)
        return

    for i in range(p, c):
        if s[i] in v:
            sol(a+1, b, i+1, d+s[i])
        else:
            sol(a, b+1, i+1, d+s[i])

l, c = map(int, input().split())
s = sorted(list(input().split()))
v = ['i', 'e', 'a', 'o', 'u']
sol(0, 0, 0, "")