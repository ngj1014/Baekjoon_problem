#반복문을 이용한 factorial
def factorial2(n):
    dap=1
    for i in range(1,n+1):
        dap*=i

    return dap

print(factorial2(6))
