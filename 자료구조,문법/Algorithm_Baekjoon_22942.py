''' 시간 초과 코드
import sys
input=sys.stdin.readline

n=int(input())


lst = []

for _ in range(n):
    lst.append(list(map(int, input().split())))

count=0
for i in range(n-1):
    if count==1:
        break
    for j in range(i+1,n):
        if (lst[i][1]+lst[j][1]<abs(lst[i][0]-lst[j][0])) or (abs(lst[i][0]-lst[j][0]) < abs(lst[i][1]-lst[j][1])) or (lst[i][0]-lst[j][0]==0 and lst[i][1]-lst[j][1] !=0 ):
            count=0
        else:
            count=1
            break

if count == 1:
    print('NO')
else:
    print('Yes')
'''

#스택을 풀어내기 -> 괄호 지우기 문제로 인식.

import sys
n = int(input())
circle = []
stack = []

for i in range(n):
    inp=sys.stdin.readline().split()
    a=int(inp[0])-int(inp[1])
    b=int(inp[0])+int(inp[1])
    circle.append([a,i,0]) #0은 여는 괄호라는 뜻 , 빼는 값 추가
    circle.append([b,i,1]) #1은 닫는 괄호라는 뜻 , 더한 값 추가

circle.sort()

for i in range(n):
    fir=circle[i][2] # 여는 괄호 무조건 임.
    if fir == 0:
        stack.append(circle[i])
    else:
        if stack[-1][2] == 0: # 전 원이 닫히지 않은 상태이면
            if stack[-1][1] == circle[i][1]: #원 번호가 같으면
                stack.pop()
            else: #원 번호가 다르면 NO를 출력해준다.
                print("NO")
                exit(0)

print("YES")


