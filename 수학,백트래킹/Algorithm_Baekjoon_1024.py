#1024번 수열의 합:내가 배운 수학으로 하진 않음..  (x+1)+(x+2)+...+(x+l)=l*x+(l*(l+1)/2)
n, l = map(int, input().split())

for i in range(l, 101):
    x = n-(i*(i+1))/2

    if x % i ==0:
        x=int(x/i)
        if x>=-1:
            for j in range(1,i+1):
                print(x + j,end=' ')
            print()
            break
else:
    print(-1)
