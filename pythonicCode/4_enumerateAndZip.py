'''
* [Boostcourse] 머신러닝을 위한 Python
* Chapter1. Pythonic Code
* 1) Pythonic Code
* 4강. Enumerate & Zip
* 2020.03.24.Tue
'''
# Enumerate: List에서 값을 추출할 때 인덱스 번호를 같이 추출
# list에 있는 index와 value를 unpacking
for i, v in enumerate(['tic', 'tac', 'toc']):
    print(i, v)

mylist = ["a", "b", "c", "d"]
# list에 있는 index와 value를 unpacking하여 list로 저장
list(enumerate(mylist)) # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]

# 문장을 list로 만들고 list의 index와 value를 unpacking하여 dict로 저장
{i:j for i,j in enumerate('Gachon University is an academic institute located in South Korea.'.split())}

# Zip: 두 개의 list 값을 병렬적으로 추출함
alist = ["a1", "a2", "a3"]
blist = ["b1", "b2", "b3"]

for a,b in zip(alist, blist):
    print(a,b) # 병렬적으로 값을 추출

# 각 tuple의 같은 index끼리 묶음
a,b,c = zip((1,2,3),(10,20,30),(100,200,300))
print(a,b,c) # (1, 10, 100) (2, 20, 200) (3, 30, 300)

# 각 tuple을 같은 index로 묶어 합을 list로 변환
list = [sum(x) for x in zip((1,2,3), (10,20,30), (100,200,300))]
print(list) # [111, 222, 333]

# Enumerate & Zip
alist = ["a1", "a2", "a3"]
blist = ["b1", "b2", "b3"]

for i, (a,b) in enumerate(zip(alist, blist)):
    print(i, a, b) # index alist[index] blist[index]를 표시
