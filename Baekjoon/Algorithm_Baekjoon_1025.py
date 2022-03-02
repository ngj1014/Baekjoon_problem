import sys
import math

M, N = map(int, sys.stdin.readline().split())

numbers = []
for _ in range(M):
    numbers.append(list(map(int, list(sys.stdin.readline().replace('\n', '')))))

#제곱수 없으면 -1 출력될 것.
result = -1


#시작점의 인덱스를 잡기위해서 m,n을 잡는다.
for m in range(M):
    for n in range(N):
        # 시작점의 인덱스를 잡기위해서 m,n을 잡는다.
        for weight_m in range(-M, M):
            for weight_n in range(-N, N):
                # 행과 열의 공차는 양수만 있는 것이아니다. -> 공차가 0인것은 조심하자. (인덱스의 weight잡는 것이다.)
                if weight_m == 0 and weight_n == 0: continue
                step = 0
                x = m
                y = n
                value = ''
                # 입력받은 수들의 범위 안에서 가능한 수열 추출
                while (0 <= x < M) and (0 <= y < N):
                    #문자열로 저장하여 한꺼번에 int로 바꾸어줄 것 -> 중요
                    value += str(numbers[x][y])
                    #step의 역할을 못잡았음 (중요!)
                    step += 1

                    #제곱수 확인
                    value_int = int(''.join(value))
                    value_sqrt = math.sqrt(value_int)
                    value_decimal = value_sqrt - int(value_sqrt)

                    #and뒤에 있는 것은 제곱수이긴하지만 직전에 구해놓은 제곱수보다 커야 저장할 필요가 있는 것.
                    if value_decimal == 0 and value_int > result:
                        result = value_int

                    x = m + step * weight_m
                    y = n + step * weight_n

print(result)

