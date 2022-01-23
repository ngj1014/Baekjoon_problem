'''상하좌우'''
n = int(input())
x=1
y=1
x = int(x)
y = int(y)

strs = input().split()

for str in strs:
    if str == 'L' or str == 'l':
        if y != 1:
            y -= 1

    if str == 'R' or str == 'r':
        if y != n:
            y += 1

    if str == 'U' or str == 'u':
        if x != 1:
            x -= 1

    if str == 'D' or str == 'd':
        if x != n:
            x += 1
print(x, y)
