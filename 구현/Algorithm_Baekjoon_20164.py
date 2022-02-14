import math

#문자열로 받으면 숫자를 굳이 쪼갤 필요가 없다.(중요)
n=input()

min_v=math.inf
max_v=0

#숫자에 홀수 몇개 있는가?
def odd_check(n: str):
    odd_n = 0
    for i in n:
        if int(i) % 2 == 1:
            odd_n += 1
    return odd_n

def solve(n,odd_n):
    global max_v,min_v

    if len(n) == 1:
        min_v=min(min_v,odd_n)
        max_v=max(max_v,odd_n)
    elif len(n) == 2:
        temp = str(int(n[0])+int(n[1]))
        solve(temp,odd_n+odd_check(temp))
    else:
        #슬라이싱을 이용하여 부분집합을 만들수 있다는 사실이 매우 중요하다.
        for i in range(len(n)-2):
            for j in range(i+1,len(n)-1):
                a=n[:i+1]
                b=n[i+1:j+1]
                c=n[j+1:]
                temp=str(int(a)+int(b)+int(c))
                solve(temp, odd_n + odd_check(temp))

solve(n,odd_check(n))
print(min_v,max_v)
