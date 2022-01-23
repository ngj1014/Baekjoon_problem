'''문자열 뒤집기 : 실제로 뒤집는 것 x /연속된 1이 많은지 연속된 0 이 많은지 봐서 적은놈선택.'''
data=input()
count0=0 #전부 0으로 만들기
count1=0 #전부 1로 만들기

if data[0] =='1':
    count0+=1
else:
    count1+=1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i]== '1':
            count0+=1
        else:
            count1+=1

print(min(count0,count1))
