#Tuples: ordered, immutable, allows duplicated elements
myTuple = ('Bui', 23, True)
print("myTuple: ", myTuple)

myTuple2 = ("Thai")
print("Type of myTuple2 when have a ele: ", type(myTuple2)) #string

myTuple2_2 = ("Thai",)
print("Type of myTuple2_2 when have a ele and a comma: ", type(myTuple2_2)) #tuple

#List to tuple
myList = ["Thai", "Bui", 23, False]
myTuple3 =tuple(myList)
print("myTuple3: ", myTuple3)
print("myTuple3[0]: ", myTuple3[0])
print("myTuple3[-2]: ", myTuple3[-2])

# myTuple3[0] = "Bui" #Error because immutable

#Loop for:
for i in myTuple3:
    print(i)

#If
if "Thai" in myTuple3:
    print("Yes")
else:
    print("No")


###
myTuple4 = ('a', 'b', 'b', 'c', 'd')
print("Length: ", len(myTuple4))
print("Count b: ", myTuple4.count('b'))
print('Index for c: ', myTuple4.index('c'))
###
#Tuple to List
myList = list(myTuple4)
print("myList: ", myList)

myTuple5 = tuple(myList)
print("myTuple5: ", myTuple5)

#####
myTuple6 = (1,2,3,4,5,6,7,8,9,10)
myTuple6_6 = myTuple6[2:5]
myTuple6_7 = myTuple6[::3]
myTuple6_8 = myTuple6[::-2]
print("myTuple6_6: ", myTuple6_6)
print("myTuple6_7: ", myTuple6_7)
print("myTuple6_8: ", myTuple6_8)

####
myTuple7  = "BUI", 23, True
name, age, bool = myTuple7
print("name: ", name)
print("age: ", age)
print("bool: ", bool)

####
myTuple8 = (0,1,2,3)

i1, *i2, i3 = myTuple8
print("i1: ", i1)
print("i2: ", i2)
print("i3: ", i3)

#Size
import sys

myListSize = [1,2,"thai", True]
myTupleSize = (1,2,"thai", True)
print("Size list: ", sys.getsizeof(myListSize), " bytes") #88 bytes
print("Size Tuple: ", sys.getsizeof(myTupleSize), " bytes") #72 bytes

#Time
import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000)) #List: 0.04012279998278245
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000)) #Tuple: 0.007813599979272112





