"""
Please take a look at the following code:

    temperatures=[10,-20,-289,100]
    def c_to_f(c):
        if c< -273.15:
            return "That temperature doesn't make sense!"
        else:
            f=c*9/5+32
            return f
    for t in temperatures:
        print(c_to_f(t))
The code prints out the output of the c_to_f  function multiple times in the terminal.

For this exercise, please write the output in a text file instead of printing it out in the terminal.

"""

# Copied code
temperatures=[10,-20,-289,100]

def c_to_f(c):
    if c< -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=c*9/5+32
        return f

new_temps = []
for t in temperatures:
    new_temps.append(c_to_f(t))

# TODO: Write to file

with open("example.txt", 'a+') as file:
    file.write("\n")
    file.write("Attempt #4:")
    file.write("\n")
    for i in new_temps:
        if isinstance(i, float):
            file.write(str(i) + "\n")


"""
Book Answer:

def writer(temperatures):
    with open("temps.txt", 'w') as file:
        for c in temperatures:
            if c>-273.15:
                f=c*9/5+32
                file.write(str(f)+"\n")

writer(temperatures) #Here we're calling the function, otherwise no output will be generated
"""
