a,b,c,d,e,f=map(int, input().split())


if a!=0 and d!=0:
    a1=a*d
    b1=b*d
    c1=c*d
    d1=d*a
    e1=e*a
    f1=f*a
    if (b1-e1) !=0 and a !=0 :
        y=(c1-f1)//(b1-e1)
        x=(c-b*y)//a

elif a == 0 and d !=0 :
    y = c//b
    x= (f-e*y)//d

if a != 0 and d ==0:
    y = f//e
    x = (c-b*y)//a
 