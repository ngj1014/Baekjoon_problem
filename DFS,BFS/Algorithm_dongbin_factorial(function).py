#recursive를 이용한 factorial: 간결한 코드가 포인트(점화식 이용.)
def factorial(n):
    if n==1 or n==0:
        return 1
    if n<0:
        return -1

    return n*factorial(n-1)

print(factorial(5))
