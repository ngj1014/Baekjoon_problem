#거스름돈
n=int(input())
mylist = [500, 100, 50, 10, 5, 1]
count=0
remainder=1000-n
for i in mylist:
    count+=remainder//i
    remainder=remainder%i

print(count)
