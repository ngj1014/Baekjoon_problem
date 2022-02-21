#입국 심사대에 몇명씩 서있는지가 중요한 포인트

n,m=map(int, input().split())

lst=[]

for _ in range(n):
    lst.append(int(input()))

lst.sort()

def Binary_Search(lst, friend_num):
    low = 1
    #중요하다..
    high = lst[0]*friend_num

    while low<=high:
        mid=(low+high)//2

        total = 0

        for i in lst:
            total += mid//i

        if friend_num<=total:
            result = mid
            high = mid - 1

        else:
            low = mid+1

    return result


print(Binary_Search(lst,m))