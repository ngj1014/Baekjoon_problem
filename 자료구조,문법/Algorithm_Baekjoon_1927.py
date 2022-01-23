#sys.stdin.readline()이 input()보다 빠르다.
#try-except구문을 보자
import heapq
import sys
n=int(input())
heap=[]
a=0
for i in range(n):
    a=int(sys.stdin.readline())

    if a!=0:
        heapq.heappush(heap, a)
    else:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap))

#        try:
#            print(heapq.heappop(heap))
#        except:
#            print(0)   #예외발생하면 여기서 해줌.
