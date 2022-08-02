hear = input()
length = len(hear)

lst = []

for i in range(length):
    a,b = hear[i],False
    lst.append([a,b])

sstr = 'quack'
dap = 0

for i in range(length):
    start = 'q'
    num = 0
    flag = False
    index = []
    for j in range(length):
        if start == lst[j][0] and lst[j][1] == False:
            index.append(j)
            num += 1
            start = sstr[num % 5]
            if start == 'q' and len(index) == 5:
                for k in index:
                    lst[k][1] = True
                flag = True
                index = []

    if flag == True:
        dap += 1

for i in range(length):
    if lst[i][1] == False:
        print(-1, end='')
        exit(0)

if dap == 0:
    print(-1, end='')
else:
    print(dap, end='')
