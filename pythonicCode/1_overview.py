'''
* [Boostcourse] 머신러닝을 위한 Python
* Chapter1. Pythonic Code
* 1) Pythonic Code
* 1강. Overview
* 2020.03.23.Mon
'''
# Pythonic Code
# Split & Join, List Comprehension, Enumerate & Zip
# 파이썬 스타일의 코딩 기법
# 파이썬 특유의 문법을 활용하여 효율적으로 코드를 표현함
# 고급 코드를 작성할 수록 더 많이 필요해짐

# 여러 단어들을 하나로 붙일 때
colors = ['red', 'blue', 'green', 'yellow']
result = ''
for s in colors:
    result += s
print(result)

# pythonic code 사용
colors = ['red', 'blue', 'green', 'yellow']
result = ''.join(colors)
print(result)
