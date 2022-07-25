n,k = map(int,input().split())
h,m,s = 0,0,0
dap=0
for i in range(n*3600+59*60+60):
    h=i//3600
    i=i%3600
    m=i//60
    s=i%60
    if s%10 == k or s//10 == k:
        dap+=1
    elif m%10 == k or m//10 == k:
        dap+=1
    elif h%10 == k or h//10 == k:
        dap+=1

print(dap)



