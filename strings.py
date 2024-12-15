# Strings: ordered, immutable, text representation

myString = "Bui Van Thai. I' m here"
myString2 = """ Hello, \
World!!!
I am Thai \\ 
I am 26 years old
I com from Nam Dinh
"""
print("myString: ", myString)
print("Length: ", len(myString))
print("myString2: ", myString2)

#########
myString3 = "Hello World"
char = myString3[0]
char2 = myString3[-2]
print("char: ", char)
print("char2: ", char2)

# myString3[1] = 'A'
# print("myString after: ", myString3) #Error, because immutable

# myString3[100] = 'X'
# print("after: ", myString3) #Error, because immutable

substring = myString3[1:4]
print("sub1: ", substring)

substring2= myString3[-2::-2]
print("sub2: ", substring2)

######
greeting = "Hello"
name = "Thai"
sentence = greeting + " " + name
print("sentence: ", sentence)

#For
for i in greeting:
    print(i)

if 'e' in greeting:
    print("Yes")
else:
    print("No")

#################
myString4 = '           Bui Van       11'
print("myString4: ", myString4)
print("Strip string: ", myString4.strip())

#
myString5 = "developER"
print("Upper: ", myString5.upper())
print("Lower: ", myString5.lower())

###endswith
myString6 = "I come from Nam Dinh"
print("endswith: ", myString6.endswith("Dinh"))
print("endswith: ", myString6.startswith("   I"))

#Find
myString7 = 'Lu do Village'
print("Find: ", myString7.find('o')) #4
print("Find: ", myString7.find('od')) #-1, because dont find

print("Count: ", myString7.count('l')) #2
print("Count: ", myString7.count('x')) #0

print("Replace: ", myString7.replace('do', 'DO'))

#######
myString8 = 'How are you doing?'
print("Split: ", myString8.split(' '))
print("Split 2 by re: ", myString8.split('re'))

myString9 = ["I", "Love", "You"]
new_string = '-'.join(myString9)
print("New string: ", new_string)

##############
from timeit import default_timer as dft
myList10 = ['T']*6
print("List 10: ", myList10)

#BAD
start = dft()
myString10_1 = ''
for i in myList10:
    myString10_1 += i
print("String 10_1: ", myString10_1)
end = dft()
print('Time1: ', end - start)

#
start2 = dft()
myString10_2 = ''
myString10_2 = ' '.join(myList10)
print("String 10_2: ", myString10_2)
end2 = dft()
print('Time2: ', end2 - start2)

###### =>>>>>>>>>>> Nếu List là 1000000 ele thì thời gian chênh lệch sẽ rõ hơn

# %, .format, f-strings

var = "Thai"
myString11 = 'the variable is %s' % var
print("myString11: ", myString11)

varNumb = 23
myString12 = 'the variable 2 is %d' % varNumb
print("variable: ", myString12)

varNumbFl = 23.08
myString13 = 'the variable 2 is %.4f' % varNumbFl
print("myString13: ", myString13)

####
abc = 3.12345
def2 = "Thai"
myString14 = "Value is: {:.2f} and {}".format(abc, def2)
print("myString14: ", myString14)

myString15 = f"The num is {abc} and name is {def2}"
print("myString15: ", myString15)

####################################################



