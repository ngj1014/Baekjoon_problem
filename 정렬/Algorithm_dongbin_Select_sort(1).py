#Array 배우기
#selecting sorting
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
min=0
for i in range(len(array)):
    min_index=i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            array[min_index], array[j] = array[j], array[min_index]

print(array)
