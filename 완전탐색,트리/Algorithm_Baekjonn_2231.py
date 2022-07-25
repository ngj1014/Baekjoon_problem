n=int(input())

for i in range(n+1):
    if i == n:
        print(0)
    dap=i
    check = i
    while(1):
        if i == 0:
            break
        check+=(i%10)
        i = i // 10

    if check == n:
        print(dap)
        break



