# Operators in python

# Types
# 1 arithmetic operators
# 2 assignment operators
# 3 comparison operators
# 4 identity operators
# 5 membership operators
# 6 bitwise operators

# 1 Arithmetic operators include:
# + Adds numbers
# - Subtracts numbers
# * Multiplies numbers
# / Divides numbers
# % - See below for explanation
# ** - See below for explanation
# // - See below for explanation

# % or modulo is will leave you with remainder

print(9 % 2)
# Prints 1 because after dividing 9 by 2 as many times as it can, there is a remainder of 1

# // or floor division will divide and round down
print(9 // 2)
# Prints 4 even tho answer is 4.5

# ** Exponentiation will have the number multiplied by itself N times
print(10 ** 3)
# Prints 1000 since 10 * 10 * 10 is 1000

#****************************************************************************************************************************
#****************************************************************************************************************************


# 2 Assignment Operators

# 1 =
# 2 += Increments number by following number
# 3 -= Decrements number by following number
# 4 *= Multiplies by following number
# 5 /= Divides number by following number
# 6 %= Assigns to remainder
# 7 **= Assigns by exponent
# 8 //= Assigns by root

#****************************************************************************************************************************
#****************************************************************************************************************************


# 3 Comparison Operators

# 1 == Compares left value to be same as the right value
# 2 != Compares left value to be different from the right value
# 3 > Compares left value to be greater than right value
# 4 >= Compares left value to be greater than or equal to right value
# 5 < Compares left value to be les than right value
# 6 <= Compares left value to be less than or equal to right value

#****************************************************************************************************************************
#****************************************************************************************************************************

# 4 Logical operators

# 1 and - Check both left AND right expression to be true
# 2 or - Check both left OR right expression to be true
# 3 not - Negates the following statement

#****************************************************************************************************************************
#****************************************************************************************************************************

# 5 Identity Operators

# is - Used to compare values to be the same
# is not - Used to compare values to be different

#****************************************************************************************************************************
#****************************************************************************************************************************

# 6 Membership Operators

# in - Used to check the value of something within a collection of data
# not in - Used to check the value of something is not within a collection of data 

x = [1,23,4,5,76]
print(2 in x)
# will print false
print(23 in x)
# will print true