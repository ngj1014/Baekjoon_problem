n=int(input())
lst=[]
for i in range(n):
    input_data=input().split(' ')
    lst.append((int(input_data[0]),input_data[1]))

#첫 번째원소로 정렬하니 나머지 원소는 순서를 그냥 지킨다라는 뜻이다.
lst=sorted(lst,key=lambda x:x[0])

for i in lst:
    print(i[0],i[1])

