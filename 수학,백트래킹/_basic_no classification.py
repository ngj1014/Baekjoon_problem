'''
n, m = map(int, input().split())
mylist = []
for i in range(n):
    mylist.append(int(input()))


mylist.sort(reverse=True)
count = 0
for i in mylist:
    if m==0:
        break
    count+=(m//i)
    m = m%i

print(count)
'''

'''
def solution(seconds):

    count=0
    count=int(count)
    if seconds==0:
        print(count)
        return 0

    count=count+(seconds//300)
    seconds=seconds%300

    if seconds==0:
        print(count)
        return 0

    count=count+(seconds//130)
    seconds=seconds%130

    if seconds==0:
        print(count)
        return 0

    count=count+(seconds//120)
    seconds=seconds%120

    if seconds==0:
        print(count)
        return 0

    count=count+(seconds//20)
    seconds=seconds%20

    if seconds==0:
        print(count)
        return 0

    else:
        print(count)
        return 0

solution(460)
'''
