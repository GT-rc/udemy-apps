"""
Please download the text file from the attachment.

Then write some code that reads the content of the file generates the following output in the command line:

pear
apple
orange
mandarin
watermelon
pomegranate
"""

file = open("fruits.txt", 'r')
content = file.read()
file.close()
print(content)
