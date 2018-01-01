"""
Please modify the code of the previous exercise so that instead of printing out the lines in the terminal, it prints out the length of each line.
"""

#Copied code (Changed to readlines):
file = open("fruits.txt", 'r')
content = file.readlines()
file.close()

#New code:
print(content)
for line_item in content:
    line_item = line_item.rstrip("\n")
    print(len(line_item))
