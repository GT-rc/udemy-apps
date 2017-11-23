greeting = "What up??!!!"
print(greeting)


# Functions
def minute_to_hours(minutes):
    hours = minutes/60.0
    return hours

def seconds_to_hours(seconds):
    return seconds / 3600

print(minute_to_hours(973))
print(seconds_to_hours(7200))
print("")
# Conditionals
# Loops
# Multiple Lists
names = ['james', 'jim', 'joe']
domains = ['gmail', 'hotmail', 'yahoo']

for i,j in zip(names, domains):
    print(i,j)

# File Handling
    # Python can read .txt and .dll
"""
# Copy of Terminal Session on reading a file:

# In Python Terminal:
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

# Open the file:
>>> file = open("example.txt", 'r')
>>> type(file)
<class '_io.TextIOWrapper'>

# Read the contents of the file:
>>> content = file.read()
>>> print(content)
Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
>>> type(content)
<class 'str'>

# Move the pointer back to the beginning of the file:
>>> file.seek(0)
0

# Read the file line by line into a list:
>>> content = file.readlines()
>>> print(content)
['Line 1\n', 'Line 2\n', 'Line 3\n', 'Line 4\n', 'Line 5\n', 'Line 6']

# Prettify the list:
>>> content1 = [i.rstrip("\n") for i in content]
>>> print(content1)
['Line 1', 'Line 2', 'Line 3', 'Line 4', 'Line 5', 'Line 6']

### THIS STEP IS VERY IMPORTANT!!! ###
# Close the file:
>>> file.close()

# Your variables that you read the data into will still be there:
>>> content
['Line 1\n', 'Line 2\n', 'Line 3\n', 'Line 4\n', 'Line 5\n', 'Line 6']
>>> content1
['Line 1', 'Line 2', 'Line 3', 'Line 4', 'Line 5', 'Line 6']
"""

# Writing to a file:
"""
# Writing lines to a file:
# Navigate to folder:
PS C:\Users\ricec\Udemy Courses> cd .\Python_Mega_Course\files\
PS C:\Users\ricec\Udemy Courses\Python_Mega_Course\files> python3

# Open Python Terminal:
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

# Opening a file that doesn't exist will create that file (note the 'w'):
>>> file=open("myexample.txt",'w')

# Write to the file directly:
>>> file.write("Line 1")
6

# Close the file to see the changes:
>>> file.close()

# Open file (which does exist this time):
>>> file=open("myexample.txt",'w')

# Write to file again - will it append?
>>> file.write("Line 2")
6

# Save and look -- no! It overwrites!
>>> file.close()

# Open it back up:
>>> file=open("myexample.txt",'w')

# This time, enter multiple lines:
>>> file.write("Line 1")
6
>>> file.write("Line 2")
6
>>> file.write("Line 3")
6

# Save and look --- everything is on one line, with no spaces but the ones you entered.
>>> file.close()

# Open again:
>>> file=open("myexample.txt",'w')

# Add content with newline characters:
>>> file.write("Line 1\n")
7
>>> file.write("Line 2\n")
7
>>> file.write("Line 3\n")
7

# That fixed that problem
>>> file.close()

# Create a list:
>>> lst = ["Line 1","Line 2","Line 3"]

# Open the file for a more convenient way to add info:
>>> file=open("myexample.txt",'w')
>>> for item in lst:
...     file.write(item+"\n")
...
7
7
7
>>> file.close()
# This time the info appears as expected with less time and trouble.
"""

# Appending to Files:
"""
# Go to the correct folder and open Python:
PS C:\Users\ricec\Udemy Courses\Python_Mega_Course\files> python3
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

# Open a file, in this case, an existing file:
>>> file = open("exercise3.txt", 'a')

# Write to the file:
>>> file.write("This has been appended!")
23
>>> file.write("This too.")
9

# Close the file:
>>> file.close()
# Lesson to remember -- include \n newline characters, it will not do it automatically.
"""

# Other File Handling Methods
"""
r   Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.
r+  Opens a file for both reading and writing. The file pointer placed at the beginning of the file.
w   Opens a file for writing only. Overwrites the file if the file already exists. If the file does not exist, it creates a new file for writing.
w+  Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist it opens a new file for both reading and writing.
a   Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
"""

# The 'With' Statement:
"""
# Open python in the correct folder:
PS C:\Users\ricec\Udemy Courses\Python_Mega_Course\files> python3
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

# Using 'with' to open the file assures that it will be closed once the operations called inside the block are complete. As usual, the variables you created with the file open, still exist.
>>> with open("example.txt", 'a+') as file:
...     file.seek(0)
...     content = file.read()
...     file.write("\nWoo!!\n")
...
0
7
>>> content
'Line 1\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6'
"""

# Section 7: More Functionalities

# Modules
