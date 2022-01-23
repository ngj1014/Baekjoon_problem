
#정렬 1) 위에서 아래로/계수정렬
n=int(input())
mylist=[]
for i in range(n):
    mylist.append(int(input()))

mylist.sort(reverse=True)

for i in range(n):
    print(mylist[i],end=' ')


#정렬2)성적이 낮은 순서대로 출력
n = int(input())
mylist=[]

for _ in range(n):
    input_data=input().split()
    mylist.append((input_data[0],int(input_data[1])))

mylist=sorted(mylist, key=lambda x : x[1])

for i in range(n):
    print(mylist[i][0],end=' ')


#정렬3) 두 배열의 원소 교체
n, k = map(int, input().split())

count = 0
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(k):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break
for i in range(n):
        count += A[i]


print(count)