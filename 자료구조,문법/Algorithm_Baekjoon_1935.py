#피연산자 만나면 push, 연산자 만나면 pop

n = int(input())
sentence = input()
alpha = [0] * n

for i in range(n):
    alpha[i] = int(input())

stack = []

for i in sentence:
    if 'A' <= i <= 'Z':
        stack.append(alpha[ord(i)-ord('A')])
    else:
        str2=stack.pop()
        str=stack.pop()

        if i == '+':
            stack.append(str+str2)
        elif i == '-':
            stack.append(str-str2)
        elif i == '*':
            stack.append(str*str2)
        elif i == '/':
            stack.append(str/str2)


print('%.2f' %stack[0])