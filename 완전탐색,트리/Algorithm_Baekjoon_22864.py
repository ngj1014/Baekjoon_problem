a,b,c,m=map(int, input().split())
dap, hp = 0, 0

for _ in range(24):
    if hp+a <= m :
        dap+=b
        hp+=a
    else:
        hp-=c
        if hp < 0:
            hp=0

print(dap)


