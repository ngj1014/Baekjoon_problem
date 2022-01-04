#백준:회의실 배정 (그리디 문제)
n = int(input())
mylist = []
count = 0
start = 0
end = 0
for i in range(n):
    mylist.append(list(map(int, input().split())))

#뒤에값기준으로 오름차순/ 그다음 앞에값기준으로 오름차순 if 내림차순하고싶으면 -x[0]처럼 앞에 -붙이기
mylist.sort(key=lambda x : (x[1],x[0]))

for i in range(n):
    if i>=1:
        if mylist[i][0] >= end:
            start = mylist[i][0]
            end = mylist[i][1]
            count+=1
    else:
        start = mylist[i][0]
        end = mylist[i][1]
        count+=1

print(count)
