'''모험가 길찾기'''
n = int(input())
scare = list(map(int, input().split()))
count = 0 #포함된 모험가의수.
group = 0
scare.sort()
for i in scare:
    count+=1
    if count>=i:
        group+=1
        count=0

print(group)
