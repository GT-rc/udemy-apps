"""
Please create some code creates a text file and writes the items of list numbers = [1, 2, 3] to that text file.
"""

numbers = [1, 2, 3]

# Create file
file = open("exercise3.txt", 'w')

# Write to the file
for item in numbers:
    file.write(str(item) + "\n")

# Close the file
file.close()
