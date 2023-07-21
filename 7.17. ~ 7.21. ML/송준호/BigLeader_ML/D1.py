# sigma_plus (for)
def sigma_plus(start,end) :
    return end+sigma_plus(start,end-1) if end > start else 0

# print(sigma_plus(0,10))

# 제곱합
# res = 0
# for i in range(1,6) :
#     res+=(i**2)
#     print(res, i)

# print(res)

# 제곱합은 비용함수로서 사용된다(== 손실함수)


# PI
# res = 1
# for i in range(1,11) :
#     res *= i
#     print(res)

#factorial
def factorial(num) :
    return (num)*factorial(num-1) if num > 1 else 1

#combination : n개 중 x개를 순서 상관 없이 뽑을 수 있는 경우의 수
def combinati(n,x) :
    return int(factorial(n)/(factorial(x)*factorial(n-x)))

# print(combinati(8,2))

#indicator function(지시 함수)
#if문 사용하여 x(예제의 경우에는 x<10)가 A에 속하는지 판단한다.

# x = 13
# if x < 10 :
#     res = 1
# else :
#     res = 0
# print(res)

#자연 상수 e (=2.718)
def e_calc(n) :
    return (1+(1/n))**n
# 수가 커질수록 2.718에 수렴함을 알 수 있다.

# min x , argmin x 
## 최솟값, 최솟값의 인덱스

## 머신러닝은 손실함수의 최솟값을 계산한다.
## min(target의 최솟값), argmin(target의 최솟값을 만드는 인자의 값)
# max x, argmax x
import numpy as np
x = [4,2,8,9,3]
# print(np.min(x),np.argmin(x),'==============',
#       np.max(x),np.argmax(x),sep='\n')


#함수의 극한
#학습과 관련해 중요한 미분 : 미분을 이해하기 위해 필요한 극한
## x->a 갈수록 f(x) -> L(값)으로 향한다는 개념.

## 좌극한과 우극한이 일치하는 경우 -> 점 a에서 극한이 존재한다.
## 좌극한과 우극한이 일치하지 않는 경우 -> a에서 극한이 존재하지 않는다.
### 극한이 존재하지 않으면 미분할 수 없고 -> 학습할 수 없다.

#미분
## x의 변화량에 대한 y의 변화량(접선의 기울기)
## 접선의 기울기를 보고 학습할 방향을 찾는다.
## 델타 -> 변화량
## lim x-> 0 x가 0으로 향하는 극한값(기울기)

# 미분은 접선의 기울기가 0까지 학습. 접선의 기울기 구하려고 하는거다. (손실함수의 최소화)

#합성함수의 미분
## 손실함수는 끊기거나 뾰족하지 않아야 한다. (지시함수 형태는 미분 불가)

#적분
## 넓이를 구하려고 한다. integral a to b f(x)dx
## 넓이 == 확률 (면적)

