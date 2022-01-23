'''시각'''
n = input()
n=int(n)
count=0
for clock in range(n+1):
    for minute in range(60):
        for second in range(60):
            if ((second//10)==3 or (second%10)==3 or (minute//10)==3 or (minute%10)==3 or (clock%10)==3):
                count+=1

print(count)
