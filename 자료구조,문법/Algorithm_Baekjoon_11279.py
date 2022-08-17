import sys
#최소힙이 기준이기에 최대힙 쓰려면 - 이용하면 된다.
import heapq
input = sys.stdin.readline
heap = []

n = int(input())

for _ in range(n):
    num = int(input())
    if num == 0:
        try:
            print(-1*heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap,-num)
'''

# 힙 직접 구현하기
from math import *
import sys

input = sys.stdin.readline


# insert
def insert(heap, num):
    heap.append(num)

    i = len(heap) - 1
    while i > 1:
        if heap[i] > heap[i // 2]:
            tmp = heap[i]
            heap[i] = heap[i // 2]
            heap[i // 2] = tmp
            i = i // 2
        else:
            break


# remove
def remove(heap):
    maxVal = heap[1]
    tmp = heap.pop()

    parent = 1
    child = 2

    while child <= len(heap) - 1:
        if child < len(heap) - 1 and heap[child] < heap[child + 1]:
            child += 1

        if heap[child] <= tmp:
            break

        heap[parent] = heap[child]
        parend = child
        child *= 2

    if len(heap) != 1:
        heap[parent] = tmp
    return maxVal


# main
n = int(input().rstrip())
heap = [0]

for _ in range(n):
    num = int(input().rstrip())

    if num == 0:
        if len(heap) == 1:
            print(0)
        else:
            print(remove(heap))

    else:
        insert(heap, num)
'''
