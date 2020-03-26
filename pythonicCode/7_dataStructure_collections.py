'''
* [Boostcourse] 머신러닝을 위한 Python
* Chapter1. Pythonic Code
* 1) Pythonic Code
* 7강. Data Structure - Collections
* Collections, Data Structure, deque, Counter, orderedDict, defaultdict, namedtuple
* 2020.03.26.Thur
'''
# Collections: List, Tuple, Dict에 대한 Python Built-in 확장 자료 구조(모듈)
# 편의성, 실행 효율 등을 사용자에게 제공함
# 아래의 모듈이 존재함
from collections import deque
from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import namedtuple

# deque: Stack과 Quque를 지원
# List에 비해 효율적인 자료 저장 방식을 지원
from collections import deque

deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(deque_list) # deque([0, 1, 2, 3, 4])

deque_list.appendleft(10)
print(deque_list) # deque([10, 0, 1, 2, 3, 4])

# rotate, reverse등 Linked List의 특성을 지원함
# 기존 list 형태의 함수를 모두 지원함
deque_list.rotate(2)
print(deque_list) # deque([3, 4, 10, 0, 1, 2])
deque_list.rotate(2)
print(deque_list) # deque([1, 2, 3, 4, 10, 0])

deque_list.extend([5,6,7])
print(deque_list) # deque([1, 2, 3, 4, 10, 0, 5, 6, 7])

deque_list.extendleft([5,6,7])
print(deque_list) # deque([7, 6, 5, 1, 2, 3, 4, 10, 0, 5, 6, 7])

print(deque_list) # deque([7, 6, 5, 1, 2, 3, 4, 10, 0, 5, 6, 7])
print(deque(reversed(deque_list))) # deque([7, 6, 5, 0, 10, 4, 3, 2, 1, 5, 6, 7])

# deque는 기존 list보다 효율적인 자료구조를 제공
# 효율적 메모리 구조로 처리 속도 향상

# General list
import time
start_time = time.perf_counter()
just_list = []
for i in range(10000):
    for i in range(10000):
        just_list.append(i)
        just_list.pop()
print(time.perf_counter() - start_time, "seconds") # 31.372754388 seconds

# deque
from collections import deque
import time

start_time = time.perf_counter()
deque_list = deque()
# Stack
for i in range(10000):
    for i in range(10000):
        deque_list.append(i)
        deque_list.pop()
print(time.perf_counter() - start_time, "seconds") # 16.18420769200003 seconds

# orderedDict
# general dictionary
d = {}
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 400

for k,v in d.items():
    print(k, v)

# orderedDict
from collections import OrderedDict
d = OrderedDict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 400

for k,v in d.items():
    print(k, v)

# Dict type의 값을, value 또는 key값으로 정렬할 때 사용 가능
for k, v in OrderedDict(sorted(d.items(), key=lambda t: t[0])).items():
    print(k,v)
for k,v in OrderedDict(sorted(d.items(), key=lambda t: t[1])).items():
    print(k,v)

# defaultdict: Dict type에 기본 값을 지정, 신규값 생성시 사용하는 방법
d = dict()
print(d["first"]) # Error

from collections import defaultdict
d = defaultdict(object) # Default dictionary를 생성함
d = defaultdict(lambda: 0) # Default 값을 0으로 설정함
print(d["first"]) # 0

# 하나의 지문에 각 단어들이 몇 개나 있는지 세고 싶을경우?
# Text-mining 접근법: Vector Space Model
text = """A press release is the quickest and easiest way to get free publicity. If well written, a press release can result in multiple published articles about your firm and its products. And that can mean new prospects contacting you asking you to sell to them....""".lower().split()

print(text)
'''
['a', 'press', 'release', 'is', 'the', 'quickest', 'and', 'easiest', 'way', 'to', 'get', 'free', 'publicity.', 'if', 'well', 'written,', 'a', 'press', 'release', 'can', 'result', 'in', 'multiple', 'published', 'articles', 'about', 'your', 'firm', 'and', 'its', 'products.', 'and', 'that', 'can', 'mean', 'new', 'prospects', 'contacting', 'you', 'asking', 'you', 'to', 'sell', 'to', 'them....']
'''

from collections import OrderedDict
word_count = defaultdict(object) # Default Dictionary 생성
word_count = defaultdict(lambda: 1) # Default 값을 1으로 설정함
for word in text:
    word_count[word] += 1

for i, v in OrderedDict(sorted(
        word_count.items(), key=lambda t: t[1],reverse=True)).items():
        print(i,v) # 값이 큰 순서대로 정렬해서 보여준다.

# Counter: Sequence type의 data element들의 갯수를 dict 형태로 반환
from collections import Counter
c = Counter() # a new, empty counter
c = Counter('gallahad') # a new counter from an iterable
print(c) # Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1}), 글자별로 count해서 보여준다.

# Dict type, keyword parameter 등도 모두 처리 가능
c = Counter({'red':4, 'blue':2}) # a new counter from a mapping
print(c) # Counter({'red': 4, 'blue': 2})
print(list(c.elements())) # ['red', 'red', 'red', 'red', 'blue', 'blue']

c = Counter(cats=4, dogs=8)
print(c) # Counter({'dogs': 8, 'cats': 4})
print(list(c.elements())) # ['cats', 'cats', 'cats', 'cats', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs']

# set의 연산들을 지원함
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d) # c-d
print(c) # Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
print(c+d) # Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2})
print(c&d) # Counter({'b': 2, 'a': 1})
print(c|d) # Counter({'a': 4, 'd': 4, 'c': 3, 'b': 2})

# word counter의 기능도 손쉽게 제공함
text = """A press release is the quickest and easiest way to get free publicity. If well written, a press release can result in multiple published articles about your firm and its products. And that can mean new prospects contacting you asking you to sell to them....""".lower().split()

print(Counter(text))
'''Counter({'and': 3, 'to': 3, 'a': 2, 'press': 2, 'release': 2, 'can': 2, 'you': 2, 'is': 1, 'the': 1, 'quickest': 1, 'easiest': 1, 'way': 1, 'get': 1, 'free': 1, 'publicity.': 1, 'if': 1, 'well': 1, 'written,': 1, 'result': 1, 'in': 1, 'multiple': 1, 'published': 1, 'articles': 1, 'about': 1, 'your': 1, 'firm': 1, 'its': 1, 'products.': 1, 'that': 1, 'mean': 1, 'new': 1, 'prospects': 1, 'contacting': 1, 'asking': 1, 'sell': 1, 'them....': 1})
'''
print(Counter(text)["a"]) # 2

# namedtuple
# Tuple 형태로 Data 구조체를 저장하는 방법
# 저장되는 data의 variable을 사전에 지정해서 저장함
from collections import namedtuple
Point = namedtuple('Point', ['x','y'])
p = Point(11, y=22)
print(p[0]+p[1]) # 33

x,y = p
print(x,y) # 11, 22
print(p.x + p.y) # 33
print(Point(x=11, y=22)) # Point(x=11, y=22)
