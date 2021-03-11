#### Day 03, 2021-03-11(Thu) Notes and Practices
# 기본자료구조 / 제어문
#### 학습목표 :  파이썬 기본자료구조의 이해와 활용
> 1. 리스트의 생성과 활용
> 2. 튜플의 생성과 활용
> 3. 딕셔너리의 생성과 활용
> 4. 세트의 생성과 활용
#### 학습목표 :  제어문의 이해와 활용
> 5. 조건제어문(if / if~ else / if elif... else)
> 6. 반복제어문(for)
> 7. 반복제어문(while)

## 1. 파이썬 기본 자료구조의 이해와 활용
파이썬은 정수, 실수, 문자열, 부울과 같은 기본 데이터 타입 외에 기본 타입들이 결합된 리스트(list), 튜플(tuple), 딕셔너리(dictionary), 세트(set) 등의 자료구조를 제공한다.   
파이썬이 제공하는 기본 자료구조에 대해서는 [파이썬 문서](https://docs.python.org/ko/3/tutorial/datastructures.html)를 참고할 수 있다.

### 1.1 리스트(list)의 생성과 활용
#### 리스트의 생성
리스트는 말 그대로 목록이라는 뜻이며, 여러 개의 값을 일렬로 늘어놓은 형태이다.   
- 리스트 만들기
변수에 값을 저장할 때 대괄호\[ \]로 묵어주면 리스크가 되며 각 값은 ,(콤마)로 구분해준다.  
리스트 = \[값, 값, 값\]
예를 들어 숫자가 3개 들어 있는 리스트를 만들고 타입을 확인해보자.
```python
lst_a = [1, 2,3]
print(lst_a)
type(lst_a)
```
리스트에 저장된 각 값은 요소(element)라고 부른다.


```python

```

- 리스트에 여러가지 자료형 동시 저장하기
리스트는 문자열, 정수, 실수, 불 등 모든 자료형을 혼합하여 저장할 수 있다. 리스트에 여러 가지 자료형을 사용하여 관련 정보를 하나로 묶기 좋다.
```python
person = ['홍길동', 19, 181.5, True]
print(person)
```


```python

```

- 빈 리스트 만들기
빈 리스트를 만들 때는 \[ \]만 지정하거나 list()를 사용한다.  
리스트 = \[ \]
리스트 = list()
```python
lst_a = [];type(lst_a)
lst_b = list();type(lst_b)
```


```python

```

- range를 사용하여 리스트 만들기  
range는 연속된 숫자를 생성하는데 range에 10을 지정하면 0부터 9까지 숫자를 생성한다.  
  + range(횟수)  
  + range(시작수, 끝수)  
  
```python
range(10)
range(0,10)
```
list()에 range를 넣어서 리스트를 생성할 수 있다.
```python
lst_a = list(range(10))
print(lst_a)
```


```python

```

#### 리스트 액세스
- 리스트 요소에 대한 접근
리스트의 요소를 사용하고자 할 때는 인덱스를 사용한다.
```python
lst_a = list(range(10))
print(lst_a[3])
```
- 슬라이싱 
리스트의 요소에 접근할 때 콜론(:)을 사용해 범위를 지정할 수도 있다.
```python
lst_a = list(range(10))
print(lst_a[3:5])
```


```python

```


#### 리스트 관련 함수  
  + append() : 리스트의 맨 뒤에 항목을 추가한다. 리스트명.append(값)
  + pop() : 리스트 맨 뒤의 항목을 삭제한다. 리스트명.pop()
  + sort() : 리스트의 항목을 정렬한다. 리스트명.sort()
  + reverse() : 리스트 항목의 순서를 역순으로 만든다.  리스트명.reverse()
  + index() : 지정한 값을 찾아 해당 위치를 반환한다.  리스트명.index(찾을값)
  + insert() : 지정한 위치에 값을 삽입한다.  리스트명.insert(위치, 값)
  + remove() : 리스트에서 지정한 값을 삭제한다. 단, 지정한 값이 여러개면 첫 번째 값만 지운다.  리스트명.remove(지울값)
  + extend() : 리스트 뒤에 리스트를 추가한다. 리스트의 더하기(+) 연산과 기능이 동일한다.  리스트명.extend(추가할리스트)
  + count() : 리스트에서 해당 값의 개수를 센다.  리스트명채.count(찾을값)
  + clear() : 리스트의 내용을 모두 지운다.  리스트명.clear()
  + del() : 리스트에서 해당 위치의 항목을 삭제한다.  del(리스트명\[위치\])
  + len() : 리스트에 포함된 전체 항목의 개수를 센다.  len(리스트명)
  + copy() : 리스트의 내용을 새로운 리스트에 복사한다.  새리스트=리스트명.copy()
  + sorted() : 리스트의 항목을 정렬해서 새로운 리스트에 대입한다.  새리스트=sorted(리스트)
  


```python

```

### 1.2 튜플의 생성과 활용
#### 튜플의 생성
리스트와 사용법이 비슷하면서도 약간 다르다. 리스트는 대괄호\[ \]로 생성하지만 튜플은 소괄호( )로 생성한다. 튜플은 값을 수정할 수 없으며, 읽기만 가능해 읽기 전용 자료를 저장할 때 사용한다.
```python
#튜플명 = (값리스트)
t1 = (1,2,3)
print(tt1)
```


```python

```

#### 튜플의 사용
튜플의 항목에 접근할 때 리스트처럼 '튜플명\[위치\]'를 사용한다.
```python
t1 = (1,2,3,4)
print(t1[1])
```
튜플 범위에 접근하려면 리스트와 마찬가지로 콜론 : 을 사용한다.


```python

```

#### 튜플과 리스트의 변환
튜플과 리스트는 서로 변환할 수 있다. 예를 들어 튜플의 항목을 변경하려면 먼저 튜플을 리스트로 변환해 항목을 변경한 후 다시 튜플로 변환하는 방법을 사용할 수 있다. list(튜플)함수는 튜플을 리스트로, tuple(리스트)함수는 리스트를 튜플로 변환해 준다.
```python
myTuple=(1,2,3)
myList=list(myTuple)
myList.append(4)
myTuple=tuple(myList)
print(myTuple)
```


```python

```

### 1.3 딕셔너리의 생성과 활용
딕셔너리는 영어 쌍 2개가 하나로 묶인 자료구조이다.  
다음과 같이 중괄호 { }로 묶어 구성하며, 키Key와 값Value쌍으로 구성되어 있다.
딕셔너리변수 = {키1:값1, 키2:값2, 키3:값3, ... }

#### 딕셔너리의 생성
```python
dic1 = {name:'홍길동', phone:'010-1234-5678', addr:'청주시 상당구'}
print(dic1)
```
#### 딕셔너리의 사용
딕셔너리는 키를 이용해 값을 구한다.
```python
print(dic1[name])
print(dic1[phone])
print(dic1[addr])
```
#### 딕셔너리 관련 함수
- 딕셔너리.get(키) : 키를 이용, 값에 접근
- 딕셔너리.keys() : 딕셔너리의 키만을 모아 dict_keys 객체를 반환
- 딕셔너리.values() : 딕녀너리의 값만을 모아 dict_values 객체를 반환
- 딕셔너리.items() : key, value 쌍 얻기
- 딕셔너리.clear() : Key:value쌍 모두 지우기
- in : 해당 키가 딕셔너리 안에 있는지 조회. ex)'키' in 딕셔너리


```python

```

### 1.4 세트의 생성과 활용
집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형
#### 집합 생성
```python
s1 = set('hello')
print(s1)
s2 = set([1,2,3])
print(s2)
```
집합 자료형은 중복을 허용하지 않으며, 순서가 없다.
#### 교집합 / 합집합 / 차집합  
set자료형을 유용하게 사용하는 경우는 교집합, 합집합, 차집합을 구할 때이다.   

```python
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
```
print(s1 & s2) #s1.intersection(s2)
print(s1 | s2) #s1.union(s2)
print(s1 - s2) #s1.difference(s2)
```  
  
#### 집합 관련 함수
  + 집합.add() : 집합에 새로운 값 추가.
  + 집합.update() : 집합에 여러 개의 값을 한꺼번에 추가
  + 집합.remove() : 집합에서 특정 값을 제거


```python

```

## 2. 제어문의 이해와 활용

파이썬 프로그램에서는 if구문과 for, while 구문을 제공한다. 다른 프로그래밍 언어와 비슷한 점도 있으나 뚜렷한 차이도 있으니 이를 구별하여 기억하도록 한다.

### 2.1 if 조건 제어문
- if문
가장 단순한 형태의 if문은 참일 때는 실행하고, 거짓일 때는 아무것도 실행하지 않는다.  
```python
a = int(input("임의 숫자 입력 : ")
if a < 100:
    print("100보다 작은 수")
print("프로그램 종료")
```

- if~else문
참일 때 실행할 문장과 거짓일 때 실행할 문장을 다르게 할 때 사용.
```python
a = int(input("임의 숫자 입력 : ")
if a < 100:
    print("100보다 작은 수")
else :
    print("100보다 큰 수")   
print("프로그램 종료")
```

- if~elif문   
동일한 형태의 조건 비교를 위한 값을 다르게 여러 차례 비교할 때

- 중첩 if문  
조건을 검사하는 과정이 2번 이상일 때.   
예를 들어 성별 연령대별 학생의 수를 카운트 한다면 다음과 같이 코딩할 수 있을 것이다.
```python
genger = input("성별을 입력하세요(M:남자/F:여자) : ")
age = int(input("나이를 입력하세요. : "))
if gender == 'M' or gender == 'm' :
    if age >= 40 :
        print("40대 이상 남자")
    elif age >= 30 : 
        print("30대 남자")
    elif age >= 20 :
        print("20대 남자")
    else:
        print("10대 이하 남자")
else :
    if age >= 40 :
        print("40대 이상 여자")
    elif age >= 30 : 
        print("30대 여자")
    elif age >= 20 :
        print("20대 여자")
    else:
        print("10대 이하 여자")    
              
```


```python

```

- 삼항 연산자를 사용한 if문  
```python
score = 55
result = ''
if score >= 60:
    result = '합격'
else :
    result = '불합격'
print(res)
```
다음과 같이 삼항 연산자를 사용해 한 줄로 줄일 수 있다.
```python
score = 50
result = ''
result = '합격' if score >= 60 else '불합격'
print(result)
```


```python

```

### 2.2 for 반복제어문
- for문의 기본 형식
```python
for 변수 in range(시작값, 끝값+1, 증가값):
    반복문
```
range()함수는 지정된 범위의 값을 반환. range(0,3,1)은 0에서 시작해 2까지 1씩 증가하는 값을 반환한다. 세번재 증가값은 생략하면 1로 인식한다.
```python
   for i in range(0,3,1):
        print("for문을 공부중입니다.")
```
range(0,3,1)은 [0,1,2]와 같다. 


```python

```

- 중첩 for문  
```python
for i in range(0,3,1):
    for k in range(0,2,1):
        print("파이썬 중첩(i값 : %d, 값:%d)"%(i,k))
```

### 2.3 while 반복 제어문
- while문의 기본형식
```python
변수 = 시작값
while 변수 < 끝값 :
    이 부분을 반복
    변수 = 변수 + 증가값
```


```python

```

- 무한 루프 while문
```python
while True:
    반복할문장
```


```python

```

- break문과 continue문
반복문에서 break문을 만나면 무조건 반복문을 벗어난다.
```python
for i in range(1,100):
    print("for문을 %d번 실행했습니다." % i)
    break
```

continue를 만나면 블록의 남은 부분을 무조건 건너뛰고 반복문의 처음으로 다시 돌아간다. 즉, 반복문을 처음부터 다시 수행한다.
```python
sum, i = 0, 0
for i in range(1,101):
    if i % 3 == 0:
        continue
    sum += i
print("1~100의 합계(3의 배수 제외) : %d" % sum)
```


```python

```
