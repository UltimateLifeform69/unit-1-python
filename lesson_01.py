"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
num_1=2.5

int_num_1=int(num_1)
# Made a variable to hold the coverted float
print(int_num_1)

"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
Num=int(input('Type a number'))
# Made the input an int
if Num>=1:
    print('Number is positive')
elif Num<0:
    print('Number is negative')
else:
    print('Number is zero')
#if statements that determine if the number is positive.
"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
my_int=5
my_float=1.5
print(my_int+my_float)
print(my_int-my_float)
print(my_int*my_float)
print(my_int/my_float)
#All of the equations are here
"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
{
    'kiwi':5,
    'apple':8
}
print(5)
"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""
burr=('burger,king,5guys')
print(burr)
bug=burr.split(',')
#The og string
burg=tuple(bug)
#The tuple 
print(burg)