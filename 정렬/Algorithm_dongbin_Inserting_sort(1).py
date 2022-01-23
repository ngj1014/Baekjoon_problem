#inserting sorting(조금더 복습이 필요하다.)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
count=1
#i는 삽일할놈,j는 그냥 비교하면서
for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j-1]>array[j]:
            array[j-1],array[j]=array[j],array[j-1]
        else:
            break
print(array)
