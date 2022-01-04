#1316번 그룹 단어 체커(처음에 check리스트 이용하려 하였으나 슬라이스를 이용한 편안한 방법)

n = int(input())
mylist=[]
count=n
for i in range(n):
    mylist.append(input())

for word in mylist:
    for j in range(len(word)-1):
        if word[j]==word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            count-=1
            break

print(count)
