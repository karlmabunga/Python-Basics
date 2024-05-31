# Use open and close methods to read files. We must close file so we don't get unexpected behavior

# First param is route to file you would like to interact with
# Second param can be: w-write r-read a-append
file = open('testfile.txt', 'r')
print(file.read())

# Reading doesn't require us to close the file

file = open('test.txt', 'w')
file.write('test\n')
file.close()

# Appending will add to the file

file = open('test.txt', 'a')
file.write('Add this line to the file\n')
file.close()

# Other methods include:

# Read Only ('r')
# Read and Write ('r+')
# Write Only ('w')
# Write and Read ('w+')
# Append Only ('a')
# Append and Read ('a+')