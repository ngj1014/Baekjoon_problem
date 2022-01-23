#수들의 합
n=int(input())
result=0
index=0
for i in range(1,100000000000):
    result += i
    if result>n:
        index = i
        print(index - 1)
        break
    else:
        continue
