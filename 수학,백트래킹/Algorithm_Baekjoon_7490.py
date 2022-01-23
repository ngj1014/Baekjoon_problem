#eval 은 input()과 다르게 문자로 입력값을 인식하지 않고, 숫자로 입력값을 인식함.
#string.replace(a,b): string의 a를 b로 바꾸어줌
import copy
def recursive(array,n):
    if len(array)==n:
        operator_list.append(copy.deepcopy(array))
        return

    array.append(' ')
    recursive(array,n)
    array.pop()

    array.append('+')
    recursive(array,n)
    array.pop()

    array.append('-')
    recursive(array, n)
    array.pop()


test_case=int(input())

for _ in range(test_case):
    operator_list=[]
    n=int(input())
    recursive([],n-1)

    integers=[i for i in range(1,n+1)]

    for operators in operator_list:
        string=""
        for i in range(n-1):
            string+=str(integers[i])+operators[i]
        string+=str(integers[-1])
        if eval(string.replace(" ",""))==0:
            print(string)
    print()







