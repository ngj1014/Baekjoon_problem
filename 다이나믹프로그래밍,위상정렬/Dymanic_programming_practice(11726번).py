#2xn 타일링 문제(11726문제) ->동적계획은 점화식을 찾아야한다.
cathe = [0] * 1001
cathe[1] = 1
cathe[2] = 2
for index in range(3,1001):
    cathe[index]= cathe[index-1]+cathe[index-2]


n=input()
n=int(n)
print(cathe[n]%10007)


