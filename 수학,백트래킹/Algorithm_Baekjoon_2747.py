#점화식은 재귀함수를 이용할 수 있다.
#그러나 반복할 때마다 연산수가 늘어나므로, dp를 사용함
def fibo(n):
    a,b=0,1
    while n>0:
        a,b=b,a+b
        n-=1
    return a
m=int(input())
print(fibo(m))