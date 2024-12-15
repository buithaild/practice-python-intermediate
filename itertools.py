# itertools: product, permutations, combinations, accumulate, groubby, and infinite iterators

from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby
myList = [1,2]
myList2 = [3,4]
myList3 =[5]
prod = product(myList,myList2)
prod2 = product(myList,myList3, repeat=2)
print("product: ", list(prod))
print("product repeat: ", list(prod2))

#permutations
#This method takes a list as an input and returns an object list of tuples that contain all permutations in a list form.
# Hoán v tất cả các vị trí trong list
myList4 = [1,2,3]
perm = permutations(myList4) #[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
print("perm: ", list(perm))

perm2 = permutations(myList4, 3) #Hoán vị cả 3 phần tử
print("perm2: ", list(perm2)) #[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

perm3 = permutations(myList4, 2) #Hoán vị cả 3 phần tử
print("perm2: ", list(perm3)) #[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

####Combinations
myList5 = [1,2,3,4,5]
comb = combinations(myList5, 2)
print("comb: ", list(comb)) #[(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]

comb = combinations(myList5, 3)
print("comb with 3: ", list(comb)) #[(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]

####### combinations_with_replacement

comb_wp = combinations_with_replacement(myList5, 2)
print("comb_wp: ", list(comb_wp))

####### accumulate
import operator
myList6 = [1,2,3,4,5]

acc = accumulate(myList6)
print("myList6: ", myList6) # [1, 2, 3, 4, 5]
print("acc: ", list(acc)) #[1, 3, 6, 10, 15]

myList7 = [1,2,3,6,100, 90, 99]
acc1 = accumulate(myList7, func=max)
print("acc with max: ", list(acc1)) #[1, 2, 3, 6, 100, 100, 100]

######Groupby
def smaller_than_101(x):
    return x < 101

myList8 = [99, 100, 101, 102]
groupbyObj = groupby(myList8, key=smaller_than_101)

groupbyObjUseLambda = groupby(myList8, key=lambda x: x < 101)
for key, val in groupbyObj:
    print(key, list(val))

for key, val in groupbyObjUseLambda:
    print(key, list(val))

# True [99, 100]
# False [101, 102

#########
person = [
    {'name': 'Thai',
     'age':26
    },
    {'name': 'Cong',
     'age': 23
     },
    {'name': 'Thanh',
     'age': 25
     }
]

groupObj = groupby(person, key = lambda x: x['age'])
for key, valxx in groupObj:
    print(key, list(valxx))

###### infinite operators

from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if i == 23:
        print("Den day thoi  >>>>>>")
        break

##
aa = [1,2,3]
for i in cycle(aa):
    print(i)
    if i == 3:
        print("Xin dung o lan thu 3")
        break

bb = [1,2,3]
for i in repeat(1, 4):
    print(i)


