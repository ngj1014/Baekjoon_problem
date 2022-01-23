#2개의 스택을 이용하면 된다.
#왼쪽 스택 , 오른쪽 스택 2개로본다.

n=int(input())
for _ in range(n):
    left_stack=[]
    right_stack=[]
    data=input()
    for i in data:
        if i =='-':
            if left_stack:
                left_stack.pop()
        elif i =='<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i=='>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)

    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))

