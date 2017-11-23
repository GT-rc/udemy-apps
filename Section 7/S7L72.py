"""
Here is a tricky exercise.

1. Please download the three text files attached in this lecture and put them in a folder. The first text file contains the text Content1 . The second contains Content2 and the third Content3 .

2. You should create a Python script that generates a new text file which should contain the content of all three text files. So the generated file should have this content:

Content1 
Content2 
Content3 

In other words, your Python script should merge the three text files. 

3. Also, the name of the output file should be the current timestamp. Example:2017-11-01-13-57-39-170965.txt 

You have some tips in the next lecture and the solution in the lecture after that.
"""

import datetime
import os

filename = datetime.datetime.now()
str_filename = str(filename)

def open_and_read(docu):
    file = open(docu, "r")
    optput = file.read()
    file.close()
    return output

def create_combined_file():
    """Combines 3 existing files."""
    file1content = open_and_read("file1.txt")
    file2content = open_and_read("file2.txt")
    file3content = open_and_read("file3.txt")

    with open(str_filename, "w") as file:
        file.write(file1content)
        file.write(file2content)
        file.write(file3content)

create_combined_file()
