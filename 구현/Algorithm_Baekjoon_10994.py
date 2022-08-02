def func(n):
    global start

    for i in range(start,4 * n - 3+start):
        for j in range(start,4 * n - 3+start):
            if i == start or j == start or i == 4 * n - 3 + start - 1 or j == 4 * n - 3 + start - 1:
                lst[i][j] = '*'
            else:
                lst[i][j] = ' '


    if n >= 3:
        start += 2
        func(n - 1)

n = int(input())
global lst
start = 0
lst = [[0] * (4*n-3) for _ in range(4*n-3)]

func(n)
lst[2*n-2][2*n-2] = '*'

for i in range(4*n-3):
    for j in range(4*n-3):
        print(lst[i][j],end='')
    if i != 4*n-4:
        print()





