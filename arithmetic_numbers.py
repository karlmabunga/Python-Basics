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


print(a)
print(type(a))
print(x)
print(type(x))
print(z)
print(type(z))