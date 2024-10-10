
"""
Task 1: Greeting
Write a function that takes a name as a 
parameter and prints a greeting message like "Hello, [name]!".
"""
def my_function(name, greeting="hello"):
    """
    To greet the name placed in the function
    """
    print(greeting + " " + name)
#Made the sentence by using the function names 
my_function("chris")
"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

def square(a):
    """
    To Square a randon number(The Power of 2)
    """
    print(a**2)

square(4)
"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""
def boo(e):
    """
    To Find whether a Number is Even or Odd
    """
    if e % 2 == 0:
        print('Even')
    else:
        print('Odd')
boo(4)

"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""
def rect(c, d):
    print(c*d)
rect(5, 8)
"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
def conv(g):
    """
    To convert Celsius to Fahrenhiet
    """
    print(g*1.8+32)

conv(5)
#Converted celsius to fahrenhiet using the equation
"""
Task 6: Average of Numbers
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""
def average(numbers):
    """
    Finds the Mean of a number
    """
    result = 0
    for x in numbers:
        result = result + x
    
    return result / len(numbers)

average([1,2,3,4,5])

"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, and returns the total.
Your function should also optionally accept a 3rd argument for discount, and return the discounted if provided.
"""

def price(m):
    """
    Discounts the price by %80
    """
    print(m*0.8)
price(5)