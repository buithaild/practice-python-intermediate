#Collections: Conter, namedtuple, OrderedDict, defaultDict, deque

from collections import Counter
a = "aaaaaaaaaaaabbbbccccccccdddd"
myCount = Counter(a)
print("My Count: ", myCount)
print("My Count-Items: ", myCount.items())
print("My Count-Values: ", myCount.values())
print("My Count-Keys: ", myCount.keys())

print("Most common: ", myCount.most_common(1))
# print("Most common [2]: ", myCount.most_common(1)[2]) #error: because not 2 ele
print("Most common 2nd: ", myCount.most_common(2))
print("Most common 3rd: ", myCount.most_common(3)) # [('a', 12), ('c', 8), ('b', 4)]
print("Most common 3rd [1]: ", myCount.most_common(3)[1]) # ('c', 8)


###########
from collections import namedtuple
point = namedtuple('Point', 'x,y')
pt = point(1, -4)
print("pt: ", pt)

Point1 = namedtuple("Testpoint", ['name', 'age', 'address'])
pt1 = Point1("Thai", 26, "Nam Dinh")
print("Index [1]: ", end="")
print(pt1[1])
print("Access addr: ", end="")
print(pt1.address)
print("Access age: ", end="")
print(pt1.age)

##################
from collections import OrderedDict,defaultdict

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print("ordered: ", ordered_dict)

ordered_dict2 = {}
ordered_dict2['x'] = 1
ordered_dict2['y'] = 2
ordered_dict2['z'] = 3
ordered_dict2['t'] = 4
print("ordered 2: ", ordered_dict2)


##defaultdict
from collections import defaultdict
d = defaultdict(int)
d['a'] = 23
d['b'] = 24
d['c'] = 25
d['d'] = 26
print("d: ", d) # defaultdict(<class 'int'>, {'a': 23, 'b': 24, 'c': 25, 'd': 26})
print("d[a]: ", d['a'])

d1 = defaultdict(float)
d1['a'] = 23
d1['b'] = 24
print("d1: ", d1) # defaultdict(<class 'float'>, {'a': 23, 'b': 24})
print("d1[a]: ", d1['a']) #23
print("d1[a]: ", d1['c']) #0.0

d2 = {}
d2['a'] = 99
d2['b'] = 100
print("d2: ", d2) #{'a': 99, 'b': 100}
print("d2[a]: ", d2['a']) #99
# print("d2[a]: ", d2['c']) # KeyError: 'c'
print("End")

#### deque
from collections import deque
d = deque()
d.append(10)
d.append(20)
d.append(30)
print("deque: ", d) #deque([10, 20, 30])

d.appendleft(40)
print("deque, appendleft: ", d) # deque([40, 10, 20, 30])"

d.pop()
print("after pop: ", d)

#clear:
d.clear()
print("clear: ",d) # deque([])
#
e = deque()
e.append(60)
e.append(70)
e.appendleft(100)
print("after appendleft: ", e) #deque([100, 60, 70])


#####################
e.popleft()
print("After popleft: ", e)

###
e.extend([200, 300])
print("extend: ", e)

e.extendleft([600, 700])
print("extend: ", e)

#rotate dịch sang bên phải bao nhiêu bước
e.rotate(1)
print("rotate 1: ", e)

e.rotate(2)
print("rotate 2: ", e)

e.rotate(3)
print("rotate 3: ", e)
e.rotate(-1)
print("rotate -1: ", e)









