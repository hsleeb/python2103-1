#### Day 03, 2021-03-11(Thu) Notes and Practices
# 제어문의 이해와 활용
#### 학습목표 :  제어문의 이해와 활용
> 1. 조건제어문(if / if~ else / if elif... else)
> 2. 반복제어문(for)
> 3. 반복제어문(while)

파이썬 프로그램에서는 if구문과 for, while 구문을 제공한다. 다른 프로그래밍 언어와 비슷한 점도 있으나 뚜렷한 차이도 있으니 이를 구별하여 기억하도록 한다.

## 1. if 조건 제어문
### if문
가장 단순한 형태의 if문은 참일 때는 실행하고, 거짓일 때는 아무것도 실행하지 않는다.  
```python
a = int(input("임의 숫자 입력 : ")
if a < 100:
    print("100보다 작은 수")
print("프로그램 종료")
```

### if~else문
참일 때 실행할 문장과 거짓일 때 실행할 문장을 다르게 할 때 사용.
```python
a = int(input("임의 숫자 입력 : ")
if a < 100:
    print("100보다 작은 수")
else :
    print("100보다 큰 수")   
print("프로그램 종료")
```

### if~elif문   
동일한 형태의 조건 비교를 위한 값을 다르게 여러 차례 비교할 때

### 중첩 if문  
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

### 삼항 연산자를 사용한 if문  
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

## 2 for 반복제어문
### for문의 기본 형식
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

### 중첩 for문  
```python
for i in range(0,3,1):
    for k in range(0,2,1):
        print("파이썬 중첩(i값 : %d, 값:%d)"%(i,k))
```

## 3. while 반복 제어문
### while문의 기본형식
```python
변수 = 시작값
while 변수 < 끝값 :
    이 부분을 반복
    변수 = 변수 + 증가값
```


```python

```

### 무한 루프 while문
```python
while True:
    반복할문장
```


```python

```

### break문 
반복문에서 break문을 만나면 무조건 반복문을 벗어난다.
```python
for i in range(1,100):
    print("for문을 %d번 실행했습니다." % i)
    break
```

### continue문
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
