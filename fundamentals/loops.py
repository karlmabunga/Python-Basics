# This file is to demonstrate how to iterate in Python

####################################################################################################################################

x = [1,2,3,4,5,6,7,8,9,10]

# print(x[0])
# print(x[1])
# print(x[2])
# print(x[3])
# print(x[4])
# print(x[5])
# print(x[6])
# print(x[7])
# print(x[8])
# print(x[9])

# Instead of manually accessing each value manually, we can use a for loop to accomplish the same thing

for item in x:
    print(item)


####################################################################################################################################

# while loops continuously will iterate while the condition remains true
# it is easy to get stuck in an infinite loop

i = 0

while i < 10:
    print(i)
    i += 1

####################################################################################################################################

# break statements terminate the execution of the loop
# continue statements skip all lines below it and move onto next iteration

str = "Hello World"

for letter in str:
    if letter == ' ':
        break
    elif letter == 'l':
        continue
    print(letter)

####################################################################################################################################

# range function

# input:
# 1 arguments means iteration start from 0 until ending with this value (non-inclusive)
# 2 arguments denote the starting iteration value and the ending value
# 3rd argument will step or how the number changes through iteration

for x in range(5):
    print(x)

for x in range(5,10):
    print(x)

for x in range(0,100, 10):
    print(x)

# iterate through string backwards

for x in range(len(str) - 1, -1, -1):
    print(str[x])
