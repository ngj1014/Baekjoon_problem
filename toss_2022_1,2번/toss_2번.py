from collections import deque
levels=[1,2,3,4]
levels=sorted(levels)
length = len(levels)
dap = -1
#print(levels)
lst=[]
q = deque(lst)
for i in range(length-1,-1,-1):
    if float((levels.index(levels[i]))/length)>=0.75:
        q.appendleft(levels[i])
    else:
        break

if len(q) == 0:
    answer = -1
else:
    answer = q[0]


answer = q[0]

print(answer)

"""
def solution(levels):
    levels=sorted(levels)
    length = len(levels)
    dap = -1
    #print(levels)

    for i in range(length):
        if float((levels.index(levels[i]))/length)>=0.75:
            answer = levels[i]
            break
    return answer
"""