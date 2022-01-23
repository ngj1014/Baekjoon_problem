#integer(오버플로우를 줄일 수 있음),float(실수오차가 조건문에서 날 수 있다.),
#string(형변환이 쉽다./immutable변수: 변경이 불가능한 변수,join함수로 +,*이용/split(),replace()활용에 초첨/slicing,char를 ord와 chr로 다루어보기,아스키코드임),boolean
#and 연산은 앞의 연산이 거짓이면 뒤에 것은 무시한다.
#join/%time함수를 알아보자:조인함수는 리스트 네의 문자열들을 결합한다.
#list,tuple(유리수 풀 때,분자 분모 따로 계산하자.),dictionary,set
#divmod(mok,remain)


#list.index( value ) : 값을 이용하여 위치를 찾는 기능
#list.extend( [value1, value2] ) : 리스트 뒤에 값을 추가 (‘+’연산자 보다 성능이 좋음)
#list.insert( index, value ) : 원하는 위치에 값을 추가
#list.sort( ) : 값을 순서대로 정렬
#list.reverse( ) : 값을 역순으로 정렬
#list = str.split() : 문자열 => 리스트, 공백시 스페이스 기준
#” “.join( list ) : 리스트에서 문자열으로

#>>> time_list
#['10', '34', '17']
#>>> ':'.join(time_list)
#'10:34:17'

#리스트 컴프리헨션 list=[i for i in range(100) if i%2==0]
#sort와 sorted의 구분:sorted는 리스트가 그대로인데 정렬되서 보여주는 것, sort는 리스트 자체를 정렬되게 바꾸어 버리는 것.
#len,sum,max,min은 O(N)의 속도임
#slicing을 이용할수 있다.

#tuple은 표현을 간결하게 할수 있다.
#a,b,c=1,2,3이렇게 표현 할 수 있다. :초기값을 설정할 때 좋다.
#a,b=map(int,input().split())

#dictionary:
#dic_test={1:2,2:3,'abc':7}
#print(dic_test.value())

#import collections

#집합은 중복을 체크해준다., 합집합,여집합,차집합등 집한연산 - 시간복잡도가 크다는 단점이 있다.