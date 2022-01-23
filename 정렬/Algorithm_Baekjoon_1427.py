#첫번째 풀이
n=list(input())
num=len(n)
n.sort(reverse=True)
print(''.join(n))
#두번쨰 풀이
array=input()
for i in range(9,-1,-1):
    for j in array:
        if int(j)==i:
            print(i, end='')