s="123"
lst=[]
for i in range(len(s)-2):
    substring = ""
    for j in range(i,i+3):
        substring+=s[j]

    if substring[0]==substring[1]==substring[2]:
        lst.append(int(substring))

if len(lst) == 0:
    print(-1)
else:
    print(max(lst))