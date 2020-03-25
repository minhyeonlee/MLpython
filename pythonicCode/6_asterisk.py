'''
* [Boostcourse] 머신러닝을 위한 Python
* Chapter1. Pythonic Code
* 1) Pythonic Code
* 6강. Asterisk
* 2020.03.25.Wed
'''
# 흔히 알고 있는 *를 의미함
# 단순 곱셈, 제곱연산, 가변 인자 활용 등 다양하게 사용됨
# *args(가변인자), tuple type
def asterisk_test(a, *args):
    print(a, args)
    print(type(args))

asterisk_test(1,2,3,4,5,6) # 1 (2, 3, 4, 5, 6), <class 'tuple'>

# **kargs(keyword인자), dict type
def asterisk_test(a, **kargs):
    print(a, kargs)
    print(type(kargs))

asterisk_test(1, b=2, c=3, d=4, e=5, f=6)# 1 {'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}, <class 'dict'>

# unpacking a container
# tuple, dict 등 자료형에 들어가 있는 값을 unpacking
# 함수의 입력값, zip 등에 유용하게 사용가능
def asterisk_test(a, *args):
    print(a, args[0]) # args[0]이 아닌 args로 찍으면 1 ((2,3,4,5,6),) 값이 나온다.
    print(type(args))
asterisk_test(1, (2,3,4,5,6)) # 1 (2, 3, 4, 5, 6), <class 'tuple'>

# 값을 풀어서 던져주기
def asterisk_test(a, args):
    print(a, *args)
    print(type(args))

asterisk_test(1, (2,3,4,5,6)) # 1 2 3 4 5 6 <class 'tuple'>

a, b, c = ([1,2,],[3,4],[5,6])
print(a,b,c) # [1, 2] [3, 4] [5, 6]

data = ([1,2],[3,4],[5,6])
print(*data) # [1, 2] [3, 4] [5, 6]

def asterisk_test(a,b,c,d,):
    print(a,b,c,d)
data = {"b":1, "c":2, "d":3}
asterisk_test(10, **data) # 10 1 2 3


for data in zip(*([1,2],[3,4],[5,6])):
    print(sum(data)) # 9 12

def asterisk_test(a,b,c,d,e=0):
    print(a,b,c,d,e)

data = {"d":1, "c":2, "b":3, "e":56}
asterisk_test(10, **data) # 10 3 2 1 56
