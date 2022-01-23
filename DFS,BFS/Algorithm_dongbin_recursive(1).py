#재귀 함수
def factorial(n):
    if n<0:
        return -1
    if n==0:
        return 1
    if n == 1:
        return 1
    result = n
    result *= factorial(n-1)
    return result

print(factorial(5))
