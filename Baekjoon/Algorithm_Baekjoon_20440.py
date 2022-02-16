#11000 강의실 배정문제랑 흡사하지만 다르다. -> 조금더 어렵다.
#입력값의 크기를 보면 for 문은 1번만 도는 것이 옳은 듯 하다.

import collections
import sys

input = sys.stdin.readline

n = int(input())
lst = list(tuple(map(int, input().split())) for _ in range(n))
lst.sort()

#중요-> 인덱스와 list를 key - value관계로 표시가능하다.
lst_check=collections.defaultdict(int)

for i in range(n):
    check_in, check_out = lst[i]
    lst_check[check_in]+=1
    lst_check[check_out]-=1

max_time=max(lst_check.keys())

mos_hot_time=[0,0]
curr_mos_cnt, next_mos_cnt = 0, 0
max_mos_cnt=0
max_first_flag = False

mos = list(lst_check.keys())
mos.sort()
for i in mos:
    next_mos_cnt = curr_mos_cnt + lst_check[i]
    #스타트점 갱신
    if next_mos_cnt > max_mos_cnt:
        max_mos_cnt =next_mos_cnt
        mos_hot_time[0]=i
        max_first_flag = True
    #예시처럼 6이 끝점과 시작점에 모두있을때 ->끝점 갱신까지는 불필요.. 그냥 연결.
    elif next_mos_cnt == max_mos_cnt and max_first_flag == True:
        mos_hot_time[1] = i
    #끝점에만 있을 때 -> 양이 감소하니까 끝점을 갱신해주는 것임.
    elif next_mos_cnt <max_mos_cnt and max_first_flag == True:
        mos_hot_time[1] = i
        max_first_flag = False

    curr_mos_cnt = next_mos_cnt



print(max_mos_cnt)
start=mos_hot_time[0]
end=mos_hot_time[1]
print(start,end)