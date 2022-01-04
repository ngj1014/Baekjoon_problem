#단어수학
import sys
n = int(sys.stdin.readline())
s = []
#AAA,AAA입력받을 2차원 배열
for i in range(n): s.append(list(input().strip()))
#알바벳은 26개가 있다. 각각의 값이 어떤 값을 갖을지 모르니 0으로 초기화
#a[0]=0 <-이다. a[0]은 10의 거듭제곱을의 합을 의미할것이다.
a = [0 for i in range(26)]
#AAA가 들어온다면 a[0]=111의 값이 저장 될 것이다.
for i in s:
    li = len(i)
    for j in range(li): a[ord(i[j]) - 65] += 10 ** (li - j - 1)
#내림차순으로 정렬해서 9부터 값을 갖음.
a.sort(reverse=True)
result, cnt = 0, 9
for i in a:
    result += cnt * i
    cnt -= 1
print(result)
