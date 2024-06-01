# Arithmetic operators
# There is a priority to operate calculations according to precedence
# Priority is as follows:
# Parentheses
# Exponents
# Multiplication
# Division
# Addition
# Subtraction

a = 3 + 5 * 6 - 4 / 2
# Expect 5 * 6 - 2 + 3 = 31

x = 5

y = ((3 + 5) * 2)** 2 / 16 - 1
# Expect (8 * 2)^2 = 256 / 16  = 16 - 1 = 15

z = x  + y


# print(a)
# print(type(a))
# print(x)
# print(type(x))
# print(z)
# print(type(z))


# Python allows you to assign a single value to several variables simultaneously.
# For example:
a=b=c=1

a = 2
b = 3
a = b
b = 4

# prints 3,4,1
# print(a)
# print(b)
# print(c)

num,name,age = 1,'KM',21

########################################################################################################################
########################################################################################################################



# Allowable characters include [a-z A-Z 0-9]
# Ex of non-allowed: @ or &

# Casting = Changing a data type from one to another

num = 2
# print(type(num))

#Won't store the type change to the variable
float(num)
# print(type(num))

#Will store the type change to the variable
num = float(num)
# print(type(num))

########################################################################################################################
########################################################################################################################


# Strings

# Methods
# These are functions that perform particular tasks for example print()
# Methods are bound to any specific data type ie. strings, number, objects

# If you want to know the methods related to any specific data type then check by typing:
# dir("string") || can be string number object or array

string = 'tIst'
string = string.upper()

string = string.replace('I', 'E')

# Strings are indexed from left to right starting at 0

# print(string)
# print(string[:2]) # will print characters from 0 to 2
# print(string[0]) # prints 'T'

# format function will format to correct type
# here numbers correlate to the arguments given to 
sentence = 'my name is {1} and my age is {0}'
name = 'Karl'
age = 21

formedSentence = sentence.format(age , name)

# print(formedSentence)

myName = f'my name is {name}'

# print(myName)

# Indexing can specifiy what in the 
list = ['develop', 'sports', 21]
testSentence = f"Hi I like to {list[0]} and play {list[1]} and my age is {list[2]}"

# print(testSentence)

########################################################################################################################
########################################################################################################################

# Lists

list = ['blue', 'green', 'red', 5, 10.5]
list.pop()
list.append(12.5)
list.remove('green')

# print(list)

########################################################################################################################
########################################################################################################################

# Tuples

# The structure of a tuple is similar to a List
# but the elements of a tuple are immutable

tuple = ('red', 'blue', 'green', 10, 0.5)

# Printing the dir('tuples') will show no mutable methods

########################################################################################################################
########################################################################################################################

# Dictionaries

# Dictionaries have a key which is a string 
# and a value which can evalutate to any type

dict = {
    'name': 'Karl',
    'age': 21
}

# print(dict.popitem())

########################################################################################################################
########################################################################################################################

# Boolean

# Can be two values either true or false

false = 5 > 10
# print(false)
# Evaluates to false

########################################################################################################################
########################################################################################################################

byte = bytes(4)
# This will create an empty bytes that is 4 bytes long
# Each byte is represented with \x followed by two hexadecimal numbers

emoji = bytes('🫡', 'utf-8')
# print(emoji)

decoded = emoji.decode('utf-8')
print(decoded)

# Bytes objects are immutable
# So if we want byte data that we can manipulate, we can use a byte array
newEmoji = bytearray('🫡', 'utf-8')
# print(newEmoji)


newEmoji[3] = int('85', 16)
print(newEmoji.decode('utf-8'))