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

# Modules, Libraries, & Packages

# Use the import statement in Python
# os -- for system commands
# dir(os) -- list of all os commands
# help(os) -- os help
# Modules and Libraries come with the default install of python, Packages are installed
# Packages use pip install command from the command prompt
# Tested pip with glob2 - worked fine!

# Commenting and Documenting Your Code
"""

Docstring goes here ----- access from the command line with: filename.__doc__ 

filename = "sample.txt"

# Created empty file
def create_file():
    with open(filename, "w") as file:
        file.write("")     # writing empty string
"""
# Putting 'r' at the beginning of the docstring will ignore special charachters in your docstring

# Working with Dates and Times

# datetime and time are the Python modules for this
# to create a file with the current date:
"""
import datetime

filename = datetime.datetime.now()
when calling filename, convert to str() ---- will still error, see below
see above
"""
# strftime.org -- strftime comes with datetime, is for formatting
# so --->  str(filename) ---> filename.strftime("%y-%d-%m")
# you can add/subtract etc with time variables using .timedelta
"""
>>> import datetime
>>> datetime.datetime.now()
datetime.datetime(2017, 11, 21, 0, 19, 39, 507327)
>>>
>>> datetime.datetime.now()
datetime.datetime(2017, 11, 21, 0, 19, 48, 702211)
>>> datetime.datetime.now()
datetime.datetime(2017, 11, 21, 0, 19, 50, 110568)
>>> datetime.datetime.now()
datetime.datetime(2017, 11, 21, 0, 19, 51, 544593)
>>> datetime.datetime.now()
datetime.datetime(2017, 11, 21, 0, 19, 52, 984228)
>>> datetime.datetime.now()
datetime.datetime(2017, 11, 21, 0, 19, 54, 24311)
>>> temp = datetime.datetime(2016, 5, 13, 11, 0, 0, 0)
>>> print(temp)
2016-05-13 11:00:00
>>> time
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'time' is not defined
>>> print(temp)
2016-05-13 11:00:00
>>> time
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'time' is not defined
>>> print(temp)
2016-05-13 11:00:00
>>> temp
datetime.datetime(2016, 5, 13, 11, 0)
>>> temp2 = datetime.datetime(2016, 12, 13, 11, 0, 0, 0)
>>> temp-temp2
datetime.timedelta(-214)
>>> temp.strftime("%Y-%m-%d")
'2016-05-13'
>>> import time
>>> lst = []
>>> for i in range(5):
...     lst.append(datetime.datetime.now())
...     time.sleep(1)
...
>>> for i in lst:
...     print(i)
...
2017-11-21 00:31:42.363897
2017-11-21 00:31:43.364377
2017-11-21 00:31:44.364855
2017-11-21 00:31:45.365045
2017-11-21 00:31:46.365767
>>>
"""

# Excercise

# Terminal Notes:
"""
Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python
Python 3.6.3 |Anaconda, Inc.| (default, Oct 15 2017, 03:27:45) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

# Opening the data file
>>> import json
>>> data = json.load(open("./data.json", 'r'))
>>> type(data)
<class 'dict'>
>>> data["rain"]
['Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.', 'To fall from the clouds in dro
ps of water.']
>>> exit()

# Return an entry
Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
['Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.', 'To fall from the clouds in dro
ps of water.']

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: rain
['Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.', 'To fall from the clouds in dro
ps of water.']

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: dsfdfg
Traceback (most recent call last):
  File "app1.py", line 14, in <module>
    print(define_word(word))
  File "app1.py", line 10, in define_word
    return data[search_key]
KeyError: 'dsfdfg'

# Verify entry is in dict and return error if it's not
Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: rain
['Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.', 'To fall from the clouds in dro
ps of water.']

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: sdfdgd
That word is not in my dictionary, sorry. Please try a different word or another resource.

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: RiAns
That word is not in my dictionary, sorry. Please try a different word or another resource.
RaIn

# Sanitize input for case.
Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ RaIn
Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: RaIn
['Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.', 'To fall from the clouds in dro
ps of water.']

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python
Python 3.6.3 |Anaconda, Inc.| (default, Oct 15 2017, 03:27:45) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> var = input("Word: ").lower()
Word: RAIN
>>> print var
  File "<stdin>", line 1
    print var
            ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(var)?
>>> print(var)
rain
>>> exit()

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: RaIN
['Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.', 'To fall from the clouds in dro
ps of water.']

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: wea9ther
That word is not in my dictionary, sorry. Please try a different word or another resource.

# Import library to assist in finding matches for mistyped words
Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python
Python 3.6.3 |Anaconda, Inc.| (default, Oct 15 2017, 03:27:45) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import difflib
>>> from difflib import SequenceMatcher
>>> SequenceMatcher(None, "rainn", "rain")
<difflib.SequenceMatcher object at 0x000002551A38D2B0>
0.8888888888888888
>>>
>>> from difflib import get_close_matches
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyboardInterrupt
>>> from difflib import get_close_matches
>>> help(get_close_matches)
Help on function get_close_matches in module difflib:

get_close_matches(word, possibilities, n=3, cutoff=0.6)
    Use SequenceMatcher to return list of the best "good enough" matches.

    word is a sequence for which close matches are desired (typically a
    string).

    possibilities is a list of sequences against which to match word
    (typically a list of strings).

    Optional arg n (default 3) is the maximum number of close matches to
    return.  n must be > 0.

    Optional arg cutoff (default 0.6) is a float in [0, 1].  Possibilities
    that don't score at least that similar to word are ignored.

    The best (no more than n) matches among the possibilities are returned
    in a list, sorted by similarity score, most similar first.

    >>> get_close_matches("appel", ["ape", "apple", "peach", "puppy"])
    ['apple', 'ape']
    >>> import keyword as _keyword
    >>> get_close_matches("wheel", _keyword.kwlist)
    ['while']
    >>> get_close_matches("Apple", _keyword.kwlist)
    []
    >>> get_close_matches("accept", _keyword.kwlist)
    ['except']

>>> import json
>>> var = json.load(open('data.json', 'r'))
>>> var_keys = var.keys()
>>> get_close_matches("rainn", var_keys)
['rain', 'train', 'rainy']
>>> get_close_matches("rainn", var_keys)[0]
'rain'
>>> exit()
Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: rain
Traceback (most recent call last):
  File "app1.py", line 18, in <module>
    word = input("Enter a word: ").lower()
KeyboardInterrupt

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: rainn
Did you mean rain?
Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: rain
['Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.', 'To fall from the clouds in dro
ps of water.']

# Added additional input to reprompt user
Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$
Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: rainn
Did you mean rain?
Enter a word: rain
None

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: rainn
Did you mean rain?
Enter a word: rain
['Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.', 'To fall from the clouds in dro
ps of water.']
None

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: rainn
Did you mean rain?
Enter a word: rain
None

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: rainn
Did you mean rain?
Enter a word: rain
['Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.', 'To fall from the clouds in dro
ps of water.']
None

# Book process for prompting the user
Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: rainn
Did you mean rain? Enter [Y] if yes, and [N] if no: y
['Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.', 'To fall from the clouds in dro
ps of water.']
Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: rainn
Did you mean rain? Enter [Y] if yes, and [N] if no: n
That word is not in my dictionary. Please try a different word or another resource.

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: rainn
Did you mean rain? Enter [Y] if yes, and [N] if no: sadf
I didn't understand that entry.

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: bbtige
That word is not in my dictionary. Please try a different word or another resource.

# Optimize output 
Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: bridge
['A structure that spans and provides a passage over a road, railway, river, or some other obstacle.', 'A system which connects
two or more local area networks at layer 2.', 'To be or make bridge over something.', 'The ridge of the nose running from the ro
ot of the nose down to the tip.', 'An elevated platform above the upper deck of a mechanically propelled ship from which it is n
avigated.', 'A wrestling move performed from a supine position, lying down face-up.']

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: bridge
A structure that spans and provides a passage over a road, railway, river, or some other obstacle.
A system which connects two or more local area networks at layer 2.
To be or make bridge over something.
The ridge of the nose running from the root of the nose down to the tip.
An elevated platform above the upper deck of a mechanically propelled ship from which it is navigated.
A wrestling move performed from a supine position, lying down face-up.

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: bridge
A structure that spans and provides a passage over a road, railway, river, or some other obstacle.
&bull;A system which connects two or more local area networks at layer 2.
&bull;To be or make bridge over something.
&bull;The ridge of the nose running from the root of the nose down to the tip.
&bull;An elevated platform above the upper deck of a mechanically propelled ship from which it is navigated.
&bull;A wrestling move performed from a supine position, lying down face-up.

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: bridge
A structure that spans and provides a passage over a road, railway, river, or some other obstacle.
&#8226;A system which connects two or more local area networks at layer 2.
&#8226;To be or make bridge over something.
&#8226;The ridge of the nose running from the  root of the nose down to the tip.
&#8226;An elevated platform above the upper deck of a mechanically propelled ship from which it is navigated.
&#8226;A wrestling move performed from a supine position, lying down face-up.

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
bridge
Enter a word: bridge
A structure that spans and provides a passage over a road, railway, river, or some other obstacle.
-A system which connects two or more local area networks at layer 2.
-To be or make bridge over something.
-The ridge of the nose running from the root of the nose down to the tip.
-An elevated platform above the upper deck of a mechanically propelled ship from which it is navigated.
-A wrestling move performed from a supine position, lying down face-up.

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: rain
Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.
To fall from the clouds in drops of water.
Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: apple
A native Eurasian tree of the genus ''Malus''.
The popular, crisp, round fruit of the apple tree, usually with red, yellow or green skin, light-coloured flesh and pips inside.

The wood of the apple tree.

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: structure
The whole of the different elements of a company organ.
Something built up of distinct parts.
To give structure to.

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: pit
Did you mean spit? Enter [Y] if yes, and [N] if no: y
['To forcefully evacuate saliva from the mouth.', 'A secretion from the salivary glands (found in the mouth) that can be spat ou
t.']

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: access road
['Any street or narrow stretch of paved surface that leads to a specific destination, such as a main highway.']

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: access road
Traceback (most recent call last):
  File "app1.py", line 30, in <module>
    print(in_dict(user_word))
  File "app1.py", line 16, in in_dict
    return sdefin[0]
NameError: name 'sdefin' is not defined

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Enter a word: access road
Any street or narrow stretch of paved surface that leads to a specific destination, such as a main highway.

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Application1-Section8 (master)
$ python app1.py
Did you mean rain? Enter [Y] if yes, and [N] if no: n
That word is not in my dictionary. Please try a different word or another resource.

"""


# Section 9: Data Analysis with Pandas

# pip install panda (comes with numpy)
# for errors, try using a precompiled python library, find the library, then your version of python, and then 32/64 bit windows verion
# ipython provides better printing of large output, install with pip

# data frame is a special object containing data
# can name columns and rows (called index)
# can use list of lists or dictionaries - with dictionaries keys will be columns
# though normally you will pull data from other files, you can make them in the program
"""
Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files/Section8 (master)
$ ipython
Python 3.6.3 |Anaconda, Inc.| (default, Oct 15 2017, 03:27:45) [MSC v.1900 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pandas
# Create a data frame
In [5]: var = pandas.DataFrame([[1,2,3,4],[5,6,7,8]])
# print it
In [6]: var
Out[6]:
   0  1  2  3
0  1  2  3  4
1  5  6  7  8
# name the columns
In [8]: var1 = pandas.DataFrame([[1,2,3],[4,5,6]], columns=["a","b","c"])

In [10]: var1
Out[10]:
   a  b  c
0  1  2  3
1  4  5  6

In [12]: type(var)
Out[12]: pandas.core.frame.DataFrame
# use methods
In [13]: var.mean()
Out[13]:
0    3.0
1    4.0
2    5.0
3    6.0
dtype: float64

In [14]: var.mean().mean()
Out[14]: 4.5

In [15]: type(var.mean())
Out[15]: pandas.core.series.Series
"""

# Getting started with Jupyter notes are in Jupyter notebook 'Testing One'

"""
Pandas may require the xlrd library as a dependency. If you get an error such as ModuleNotFoundError: No module named 'xlrd'  you can fix that by installing xlrd:

pip install xlrd 
"""

# Panda notes are in Jupyter Notebook 'Testing One'


# Section 10: Numpty

# 
"""
Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files (master)
$ pip install opencv-python
Collecting opencv-python
  Downloading opencv_python-3.3.0.10-cp36-cp36m-win_amd64.whl (39.7MB)
Requirement already satisfied: numpy>=1.11.3 in c:\programdata\miniconda3\lib\site-packages (from opencv-python)
Installing collected packages: opencv-python
Successfully installed opencv-python-3.3.0.10

Janet@BenderIsGreat-LAPTOP MINGW64 ~/CodeStuff/UdemyCode/Python_Mega_Course/files (master)
$ python
Python 3.6.3 |Anaconda, Inc.| (default, Oct 15 2017, 03:27:45) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import cv2
>>>
"""