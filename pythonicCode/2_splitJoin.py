'''
* [Boostcourse] 머신러닝을 위한 Python
* Chapter1. Pythonic Code
* 1) Pythonic Code
* 2강. Split and Join
* 2020.03.23.Sun
'''
# Split 함수 : String Type의 값을 나눠서 List 형태로 변환
# 뉴스 데이터 등(BoW)에서 어떤 단어가 얼마나 포함되어있는지 확인할 때 사용 많이함.
items = 'zero one two three'.split() # 빈칸을 기준으로 문자열 나누기
print(items)

example = 'python, jquery, javascript'# ","을 기준으로 문자열 나누기
example.split(",")
print(example)

a,b,c = example.split(",")
# 리스트에 있는 각 값을 a, b, c 변수로 unpacking
example = 'cs50.gachon.edu'
subdoma, domain, tld = example.split(".")

# Join 함수: String List를 합쳐 하나의 String으로 반환할 때 사용.
colors = ['red', 'blue', 'green', 'yellow']
result = ''.join(colors)
print(result)

result = '.'.join(colors)
print(result)

result = ', '.join(colors)
print(result)

result = '-'.join(colors)
print(result)
