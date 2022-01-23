#quick sorting은 pivot을 이용한 정렬 pivot왼쪽은 모두 pivot보다 작고, 오른쪽은 크다.
array=[5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array,start,end):
    if start>=end: #원소가 1개인 경우
        return
    pivot=start
    left=start+1
    right=end
    while left<=right:
        while left<=end and array[left]<=array[pivot]:
            left+=1
        while right>start and array[right]>=array[pivot]:
            right-=1
        if left>right:
            array[right],array[pivot]=array[pivot],array[right]
        else:
            array[right],array[left]=array[left],array[right]
        quick_sort(array,start,right-1)
        quick_sort(array,right+1,end)