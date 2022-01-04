n=int(input())
a=map(int, input().split())

m=int(input())
b=map(int,input().split())

a=list(a)
b=list(b)
a.sort()
def binary_search(value,start,end):
    if start>end:
        return False
    median=(start+end)//2
    if value<a[median]:
        return binary_search(value,start,median-1)
    elif value>a[median]:
        return binary_search(value,median+1,end)
    else:
       return True

for item in b:
    if binary_search(item,0,n-1):
        print(1)
    else:
        print(0)
