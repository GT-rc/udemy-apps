"""
Create a function that converts Celsius degrees to Fahrenheit. The formula to convert Celsius to Fahrenheit is F = C × 9/5 + 32.
"""

def celcius_to_farenheit(degrees):
    farenheit = degrees * (9/5) + 32
    return farenheit

print(celcius_to_farenheit(19))
