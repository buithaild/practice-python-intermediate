# Sets: unordered, mutable, no duplicates

mySet = {1,2,3,4,5}
mySetDup = {1,2,3,4,3,2}
print("mySet: ", mySet) #{1, 2, 3, 4, 5}
print("mySetDup: ", mySetDup) #{1, 2, 3, 4}

mySet1 = set([7,8,"Hello", True])
print("mySet1: ", mySet1) #{8, True, 'Hello', 7}

mySet2 = set("Bui Thai")
print("mySet2: ", mySet2) #{'B', 'h', 'a', 'i', 'u', 'T', ' '}

mySet3= {}
print("Type of mySet3: ", type(mySet3)) #<class 'dict'>

#Add
mySet4 = set()

mySet4.add(1)
mySet4.add(2)
mySet4.add(3)
print("mySet4: ", mySet4)

#Remove
mySet5 = {7,8,9,10}
mySet5.remove(10)
print("mySet5: ", mySet5)

# mySet5.remove(11)
# print("mySet5: ", mySet5) #Error because not ele 11

#Discart
mySet6 = {7,8,9,10}
mySet6.discard(9)
print("mySet6 disCart 6: ", mySet6)
mySet6.discard(100)
print("mySet6 discard 100: ", mySet6)

#Pop
mySet7 = {5,6,7,8}

print("pop: ", mySet7.pop())
print("mySet after: ", mySet7)

#For

mySet8 = {5,6,7,8}

for x in mySet8:
    print("x: ", x)

#IF
if 9 in mySet8:
    print("Yes")
else:
    print("No")

##########
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

u = odds.union(evens)
print("onion: ", u)

i = odds.intersection(primes)
print("intersection: ", i)

i2 = evens.intersection(primes)
print("intersection 2: ", i2)

#Diff
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

diff = setA.difference(setB)
print("Diff: ", diff)

#Symmetic difference
setC = {1,2,3,4,5,6,7,8,9}
setD = {1,2,3,10,11,12}

sd = setD.symmetric_difference(setC)
print("symmetric diff: ", sd)

#Update
setE = {1,2,3,4,5,6,7,8,9}
setF = {1,2,3,10,11,12}

setE.update(setF)
print("setE: ", setE)

setE2 = {1,2,3,4,5,6,7,8,9}
setF2 = {1,2,3,10,11,12}
setE2.intersection_update(setF2)
print("inter_update: ", setE2)

###############
setG = {1,2,3,4,5,6,7,8,9}
setH = {1,2,3,10,11,12}

setG.difference_update(setH)
print("setG: ", setG)

#####
setI = {1,2,3,4,5,6,7,8,9}
setK = {1,2,3,10,11,12}

setI.symmetric_difference_update(setK)
print("synmmetric diff update: ", setI)

#########
set9 = {1,2,3,4,5,6,7,8}
set10 ={1,2,3}
set11 ={9,10}

print("isSuperSet: ", set9.issuperset(set10))
print("isdisjoin 1: ", set9.isdisjoint(set10)) #False
print("isdisjoin 2: ", set9.isdisjoint(set11)) #True

######################

set12 = {97, 98, 99, 100}

set13 = set12
set13.add(101)
print("set12: ",set12) #{97, 98, 99, 100, 101} because ta gán 2 set như nhau => dùng set()
print("set13: ",set13) #{97, 98, 99, 100, 101}

set14 = set(set12)
set14.add(102)
print("set12: ",set12)
print("set14: ",set14)

# ++++++++++++++
a = frozenset([1,3,5,7])

# a.add(9) #Error:
# print(a)

# a.remove(9) #Error:
# print(a)





