A=int(input()) #사람수 0~(n-1)
#T번째 뻔(0) 외치거나 T번째 데기(1)외치거나
T=int(input())
number = int(input())

bundaegi = []
bun = daegi = 1
turn = 0

while(1):
    turn += 1
    for _ in range(2):
        bundaegi.append((bun,0))
        bun += 1
        bundaegi.append((daegi,1))
        daegi += 1

    for _ in range(turn+1):
        bundaegi.append((bun,0))
        bun += 1

    for _ in range(turn+1):
        bundaegi.append((daegi,1))
        daegi += 1

    if T <= bun:
        print(bundaegi.index((T,number))%A)
        break





