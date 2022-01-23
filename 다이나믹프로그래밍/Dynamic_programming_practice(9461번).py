#파도반 수열(9461번)
cathe = [0] * 101
cathe[1] = 1
cathe[2] = 1
cathe[3] = 1

for index in range(4,101):
    cathe[index]= cathe[index-3]+cathe[index-2]

number=input()
number=int(number)
for i in range(number):
    n=input()
    n=int(n)
    print(cathe[n])

