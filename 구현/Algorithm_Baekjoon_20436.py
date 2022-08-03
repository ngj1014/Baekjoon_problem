left, right = input().split()
strings = list(input())

keyboard = ["qwertyuiop","asdfghjkl","zxcvbnm"]
mo = "yuiophjklbnm"

x1,y1,xr,yr = None, None, None, None

for i in range(len(keyboard)):
    if left in keyboard[i]:
        x1 = i
        y1 = keyboard[i].index(left)
    if right in keyboard[i]:
        xr = i
        yr = keyboard[i].index(right)

time = 0

for string in strings:
    time+=1
    if string in mo:
        for i in range(len(keyboard)):
            if string in keyboard[i]:
                nx = i
                ny = keyboard[i].index(string)

                time += abs(nx-xr) + abs(ny-yr)
                xr = nx
                yr = ny
                break
    else:
        for i in range(len(keyboard)):
            if string in keyboard[i]:
                nx = i
                ny = keyboard[i].index(string)

                time += abs(nx-x1) + abs(ny-y1)
                x1 = nx
                y1 = ny
                break

print(time)