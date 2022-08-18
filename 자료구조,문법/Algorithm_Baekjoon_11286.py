import sys
import heapq
import math
input = sys.stdin.readline
heap = []
heap_2 = []
n = int(input())

for _ in range(n):
    k = int(input())
    #최소 힙
    if k>0:
        heapq.heappush(heap,k)
    #최대 힙
    elif k<0:
        heapq.heappush(heap_2,-k)
    elif k == 0:
        if len(heap) != 0 and len(heap_2) != 0:
            if heap[0]>=heap_2[0]:
                print(-1*heapq.heappop(heap_2))
            elif heap[0]<heap_2[0]:
                print(heapq.heappop(heap))
        elif len(heap) != 0 and len(heap_2) == 0:
            print(heapq.heappop(heap))
        elif len(heap) == 0 and len(heap_2) != 0:
            print(-1 * heapq.heappop(heap_2))
        elif len(heap) == 0 and len(heap_2) == 0:
            print(0)
