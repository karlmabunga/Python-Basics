# This file is a quick introduction to functions and methods like input

####################################################################################################################################

# a = input('write the first value')
# b = input('write the second value')

# Casting to change the data types
# a = int(a)
# b = int(b)

# c = a + b

# print(c)

####################################################################################################################################


# c = input("Enter the temperature in celcius")
# c = int(c)
# fahrenheit = (9/5)*c + 32

# print(fahrenheit, 'degrees F')

# function version of above

# def printCelcius(num):
#     f = (9/5)*int(num) + 32
#     return print('This is ', f, ' degrees F')

# printCelcius(input('Enter degrees in Celcius'))

####################################################################################################################################

# m = input('Input minutes')
# s = input('Enter seconds')

# h = int(m)/60 + int(s)/3600
# print('This translated to ', h, ' hours')

# def convertHours(m, s):
#     return print('This was converted to ',int(m)/60 + int(s)/3600, ' hours')

# convertHours(input('Enter minutes to convert to hours'), input('Enter seconds to convert to hours'))

####################################################################################################################################

# def keyword is the keyword used to define a function
# you can add default values to parameters by adding = followed by default value

# def add(x=0, y=0):
#     return print(x + y)

# # we can use the input method to use the input variables given to us by user

# var1 = input('Enter first value to add')
# var2 = input('Enter second value to add')

# add(int(var1), int(var2))

####################################################################################################################################

# Example of handling an edge case

# def div(a, b):
#     if (int(b) == 0):
#         return print('Invalid second agruement')
#     return print(int(a)/int(b))

# div(input('Enter first value'), input('Enter second value'))