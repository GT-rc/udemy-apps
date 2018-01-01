"""
In one of the previous exercises we create the following function:

    def string_length(mystring):
        return len(mystring)

Calling the function with a string as input will return the length of that string. However, if you pass an integer:

    string_length(10)

That would generate an error since the len()  function doesn't work for integers.

Your duty is to modify the function so that if an integer is passed as an input, the function should output a message like "Sorry integers don't have length".

"""

def string_length(mystring):
    if type(mystring) == str:
        return len(mystring)
    else:
        return "Sorry, that is not a string!"

print(string_length("Hello!"))
