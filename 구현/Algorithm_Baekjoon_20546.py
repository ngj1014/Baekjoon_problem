import sys
input = sys.stdin.readline

input_money = int(input())
machine_duck = list(map(int,input().split()))

j_cash, s_cash = input_money, input_money
j_stock, s_stock = 0,0

for i in machine_duck:
    if j_cash>=i:
        j_stock += j_cash//i
        j_cash %= i


for i in range(len(machine_duck)-3):
    if machine_duck[i] > machine_duck[i+1] > machine_duck[i+2]:
        s_stock += s_cash // machine_duck[i+3]
        s_cash %= machine_duck[i+3]

    elif machine_duck[i] < machine_duck[i+1] < machine_duck[i+2]:
        s_cash += s_stock * machine_duck[i+3]
        s_stock = 0

j_asset = j_cash + (machine_duck[-1] * j_stock)
s_asset = s_cash + (machine_duck[-1] * s_stock)

if j_asset > s_asset:
    print('BNP')
elif j_asset < s_asset:
    print('TIMING')
else:
    print('SAMESAME')

