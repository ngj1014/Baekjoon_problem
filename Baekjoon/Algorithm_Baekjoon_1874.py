#스택->push,pop을 이용해서 푼다. / LIFO자료 형태이다.
#스택의 마지막항은 stack[-1]이다.
n=int(input())
stack=[]
result=[]
count=0
num=0
X=True

for _ in range(n):
    count=int(input())
    while num<count:
        num+=1
        stack.append(num)
        result.append("+")

    if stack[-1]==count:
        stack.pop()
        result.append("-")

    else:
        X=False
        break


if X==True:
    for i in result:
        print(i)
else:
    print("NO")
