'''
* [Boostcourse] 머신러닝을 위한 Python
* Chapter1. Pythonic Code
* 1) Pythonic Code
* 3강. List Comprehension
* 2020.03.23.Mon
'''
# List comprehensions
# 기존 List를 사용하여 간단히 다른 List를 만드는 기법
# 포괄적인 List, 포함되는 리스트라는 의미로 사용됨
# 파이썬에서 가장 많이 사용되는 기법 중 하나
# 일반적으로 for + append 보다 속도가 빠름

# 일반적인 for loop
result = []
for i in range(10):
    result.append(i)
print(result) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# List Comprehension
result = [i for i in range(10)]
print(result) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Filter 사용(조건 사용)
result = [i for i in range(10) if i % 2 ==0]
print(result) # [0, 2, 4, 6, 8]

# Nested For Loop(result = 1 dimensional list)
word_1 = "Hello"
word_2 = "World"
result = [i+j for i in word_1 for j in word_2]
print(result)

case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]
result = [i+j for i in case_1 for j in case_2]
print(result)

# Filter : i랑 j가 같지 않을 때만 추가함
result = [i+j for i in case_1 for j in case_2 if not(i==j)]
print(result)
result.sort()
print(result)

# 문장을 빈칸 기준으로 나눠 list로 변환
words = "The quick brown fox jumps over the lazy dog".split()
print(words)

# list의 각 elements들을 대문자, 소문자, 길이로 변환하여 two dimensional list로 변환
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
for i in stuff:
    print(i)

case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "F"]
# 1 Dimensional
result = [i+j for i in case_1 for j in case_2]
print(result)

# 2 Dimensional
result = [[i+j for i in case_1] for j in case_2]
print(result)
