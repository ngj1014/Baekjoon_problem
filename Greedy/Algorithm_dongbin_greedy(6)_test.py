'''곱하기 혹은 더하기'''
data_list = map(int, input().split())
dap = 1
count=0
for i in data_list:
    if i == 0:
        continue
    if dap==1:
        if count==0:
            dap=0
            count+=1
        dap+=i
    else:
        dap*=i
print(dap)
