import sys

n = int(input())
lst = []

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        lst.append(command[1])
    elif command[0] == 'pop':
        if len(lst) != 0:
            print(lst.pop())
        else:
            print('-1')
    elif command[0] == 'size':
        print(len(lst))

    elif command[0] == 'empty':
        if len(lst) == 0:
            print('1')
        else:
            print('0')

    elif command[0] == 'top':
        if len(lst) != 0:
            print(lst[-1])
        else:
            print('-1')
