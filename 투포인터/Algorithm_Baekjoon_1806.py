import sys
input = sys.stdin.readline

n, s = map(int, input().split())
lst = list(map(int, input().split()))

#합계를 미리 구해 놓는 과정이 중요하다 . sum함수를 사용하면 시간이 오래 걸림.
sum_lst = [0] * (n+1)
for i in range(1, n+1):
    sum_lst[i] = sum_lst[i-1] + lst[i-1]

answer = 1000001
start = 0
end = 1

while start !=n :
    if sum_lst[end]-sum_lst[start] >= s:
        if end - start<answer:
            answer=end-start
        start+=1

    else:
        if end != n:
            end += 1
        else:
            #의미 없는 것이 계속하다보면 start가 n이 되어 끝나게됨.
            start+=1

if answer !=1000001:
    print(answer)
else:
    print(0)