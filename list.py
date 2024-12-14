# List: ordered, multable, allows duplicate elements

myList1  = ["banana", "cherry", "apple"]
print("myList: ", myList1)

myList2 = list()
print("myList2: ", myList2)

myList3 = [True, 5, "laptop", [1,2,3], (4,5,6)]
print("myList3: ", myList3)

item = myList1[1]
print("item: ", item)

#loop
for i in myList1:
    print("ele:  ", i)

if "banana" in myList1:
    print("Yes")
else:
    print("No")
print("======================")
if "lemon" in myList1:
    print("Yes")
else:
    print("No")

#Length of List
print("Length of myList1: ", len(myList1))

#Add element to list
myList1.append("lemon")
print("new myList: ", myList1)

#Insert
myList1.insert(1, "orange")
print("After insert orange: ", myList1)

myList1.insert(6, "lychee")
print("After insert lychee: ", myList1)

myList1.insert(10, "grapefruit")
print("After insert grapefruit: ", myList1)

#pop
item2 = myList1.pop()
print("Item2: ", item2)
print("After pop: ", myList1)

#Remove
item3 = myList1.remove("cherry")
print("item3: ", item3)
print("After remove cherry, myList1: ", myList1)


# item4 = myList1.remove("grapefruit") # error: because grapefruit is removed
# print("After remove grapefruit, myList1: ", myList1)

# Clear
# item5 = myList1.clear()
# print("item5: ", item5)
# print("After clear: ", myList1)

#Reverse
item6 = myList1.reverse()
print("After reserve: ", myList1)

#Sort
myLis1_1 = myList1.sort()
print("After sort: ", myList1)

exam = [4,2,-6,1111,3,6,2]
new_exam =exam.sort()
print("After sort, example: ", exam)


exam2 = [5,2,3,1,10]
print("exam2: ", exam2)
new_exam2 = sorted(exam2)
print("After sort, example2 : ", new_exam2)

##########
myList4 = [0] * 5
print("myList4: ", myList4)
#Add list
myList5 = [1,2,3,4,5]
newList5 = myList5  + myList4
print("newList: ", newList5)

#Access:
myList6  = [1, 2, 3, 4, 5, 6, 7]
a = myList6[1:4]
print("a: ", a)
b = myList6[:4]
print("b: ", b)
c = myList6[1::2]
print("c: ", c)

d = myList6[::-1]
print("d: ", d)

list_org = ["banana", "cherry", "lemon"]

list_cpy = list_org
print("list_cpy: ", list_cpy)
list_cpy.append("grape")
print("list_org: ", list_org) #list_org se thay doi theo cung voi cpy => su dung copy()
print("list_cpy after append: ", list_cpy)

list_org1 = ["a", "b", "c"]
list_cpy1 = list_org1.copy()
list_cpy2 = list(list_org1) #list_org se thay doi theo cung voi cpy
print("list_org1: ", list_org1)
print("list_cpy2: ", list_cpy2)

list_cpy1.append("d")
print("list_cpy1: ", list_cpy1)

#Loop

myList7 = [1,2,3,4,5,6]
b = [i*i for i in myList7]

print("myList7: ", myList7)
print("after, myList7: ", b)



