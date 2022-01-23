#계수정렬: 범위가 1~10000까지 적을때 사용할수 있다.  -> 인덱스번호에 대해 값으로 보내겠다.
#데이터 개수가 많을때, sys.stdin.readline()을 써야한다.
import sys
n=int(sys.stdin.readline())
array=[0]*10001

for i in range(n):
    data=int(sys.stdin.readline())
    array[data]+=1



for i in range(10001):
    if array[i]!=0:
        for j in range(array[i]):
            print(i)