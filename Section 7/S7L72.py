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

new_file = datetime.datetime.now().strftime('%Y-%b-%d--%H-%M')

def open_and_read(docu):
    """Opens and reads a file into a variable, closes file and returns variable containins info."""
    file = open(docu, "r")
    output = file.read()
    file.close()
    return output

def create_combined_file():
    """Combines 3 existing files."""
    # file1content = open_and_read("file1.txt")
    # file2content = open_and_read("file2.txt")
    # file3content = open_and_read("file3.txt")

    filenames = ['./file1.txt', './file2.txt', './file3.txt']

    with open(new_file, "w") as outfile:
        for fname in filenames:
            with open(fname, 'r') as infile:
                outfile.write(infile.read() + "\n")
    # print(type(new_file))
    return new_file

# def main():
#     """Main"""
#     print("...starting")
#     try:
#         f = create_combined_file()
#         with open(f) as file:
#             text = f.read()
#             print(text)
#     except FileNotFoundError:
#         print("It didn't work, dodo.")

# main()

create_combined_file()
