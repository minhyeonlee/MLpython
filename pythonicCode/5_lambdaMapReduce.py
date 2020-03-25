'''
* [Boostcourse] 머신러닝을 위한 Python
* Chapter1. Pythonic Code
* 1) Pythonic Code
* 5강. Lambda & Map & Reduce
* 2020.03.25.Wed
* Lambda, map, reduce는 간단한 코드로 다양한 기능을 제공
* 그러나 코드 직관성이 떨어져서 lambda나 reduce는 python3에서 사용을 권장하지 않음
* Legacy library나 다양한 머신러닝 코드에서 여전히 사용중
'''
# Lambda: 함수 이름 없이, 함수처럼 쓸 수 있는 익명함수(수학의 람다 대수에서 유래함)
# Python3 부터는 권장하지 않으나 여전히 많이 쓰임
# General function
def f(x,y):
    return x+y
print(f(1,4)) # 5

# Lambda function
f = lambda x,y: x+y
print(f(1,4)) # 5

f = lambda x: x**2
print(f(3)) # 9

f = lambda x: x/2
print(f(3)) # 1.5

print((lambda x: x+1)(5)) # 6

# Map Function
# Sequence 자료형 각 element에 동일한 function을 적용함
ex = [1,2,3,4,5]
f = lambda x: x**2
print(list(map(f, ex))) # [1, 4, 9, 16, 25]

f = lambda x,y: x+y
print(list(map(f, ex, ex))) # [2, 4, 6, 8, 10]

# 두 개 이상의 list에도 적용 가능함, if filter도 사용가능
ex = [1,2,3,4,5]
f = lambda x,y: x+y
print(list(map(f, ex, ex))) # [2, 4, 6, 8, 10]

list(map(
    lambda x: x**2 if x%2 == 0 else x, # else를 반드시 넣어줘야함
    ex
    )) # [1, 4, 3, 16, 5]

# list comprehension으로 위와 같이 할 수 있음(python3)
[value**2 for value in ex] # [1, 4, 9, 16, 25]

# python3는 iteration을 생성 -> list를 붙여줘야 list 사용가능
# 실행시점 값을 생성, 메모리 효율적
ex = [1,2,3,4,5]
print(list(map(lambda x: x+x, ex))) # [2, 4, 6, 8, 10]
print(map(lambda x: x+x, ex)) # python3에서는 <map object at 0x107668b50>

f = lambda x: x**2
print(map(f, ex)) # python3에서 <map object at 0x107668b50>

for i in map(f, ex): # 1, 4, 9, 16, 25
    print(i)

# Reduce function
# map function과 달리 list에 똑같은 함수를 적용해서 통함
from functools import reduce
print(reduce(lambda x,y: x+y, [1,2,3,4,5])) # 15

def factorial(n):
    return reduce(
        lambda x,y: x*y, range(1, n+1)
    )
print(factorial(5)) #120
