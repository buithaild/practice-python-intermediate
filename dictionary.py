# Dictionary: Key- Value pairs, Unordered, mutable

myDict1 = {
    "name": "Thai",
    "age": 25,
    "isMarried": False
}

print("myDict1: ", myDict1)

myDict2 = dict(name = "Bui", age = "26", isMarried = True)
print("myDict2: ", myDict2)

value_name = myDict1["name"]
print("Name: ", value_name)

# value_name_full = myDict1["nameFull"]
# print("Name full: ", value_name_full) #Error

myDict1["email"] = "buithai@gmail.com"
print("My dict1, after: ", myDict1)

myDict1["email"] = "buithaild230899@gmail.com"
print("My dict1, after: ", myDict1)

#Delete
del myDict1["name"]
print("After del: ", myDict1)

#Pop
myDict1.pop("age")
print("After pop: ", myDict1)

# Del phan tu cuoi
myDict1.popitem()
print("After popitem: ", myDict1)


#
myDict3 = {'name': 'Thai', 'age': 25, 'isMarried': False, 'email': 'buithaild230899@gmail.com'}
if "name" in myDict3:
    print(myDict3["name"])

if "lastName" in myDict3:
    print(myDict3["lastName"])

##
try:
    print(myDict3["nameFull"])
except:
    print("Error")

#Loop
for key in myDict3:
    print(key)

for key in myDict3.keys():
    print(key)

for val in myDict3.values():
    print(val)

print("------------------------------")
for key, val in myDict3.items():
    print(key, ": ", val)

print("======================>>")
myDict_cpy = myDict3 #Gán lại y hệt, be carefull when use

print("myDict3 init: ", myDict3)
print("Copy: ", myDict_cpy)

myDict_cpy["email"] = "thai_copy@gmail.com"
print("myDict_cpy: ", myDict_cpy)
print("after, myDict3: ", myDict3)

print("$$$$$$$")
myDict_cpy_2 = dict(myDict3)
myDict_cpy_2["email"] = "thai_update@gmail.com"
print("myDict_cpy_2: ", myDict_cpy_2)
print("after, myDict3: ", myDict3)

#############
myDict4 = dict(name = "Bui", age = 25, job = "Developer")
myDict5 = {'name': 'Messi', 'age': 38, 'isMarried': True}
myDict4.update(myDict5)
print("after updated, myDict4: ", myDict4)

##########3
myDict6 = {3: 9, 6: 36, 9: 81}
print("myDict6: ", myDict6)

# val = myDict6[0] #Error
val1 = myDict6[3]
print("Val1: ", val1)

#
myTuple = (8,  7)
myList = [1,2]
myDict8 = {myTuple: 56, "hello": myList}
# myDict7 = {myTuple: 56, myList: 3} #Error, because myList is multable, is not key in dict
print("myDict8: ", myDict8) # {(8, 7): 56, 'hello': [1, 2]}


