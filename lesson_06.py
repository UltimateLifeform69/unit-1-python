"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
i=0
while i<10:
    i+=1
    print(i)
# Made i=0 so that 10 would be counted then made a while loop that added 1 and stopped at 10
"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
a=11
while a>1:
    a-=1
    print(a)
# I reversed 1
"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
x=float(input('choose a number and I will do a factorial equation '))
y=10
while y>=1:
    x=x*y
    y-=1

print(x)
"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
word="boruto"
guess=input("What is your password? ")

while guess!=word:
    print('incorrect. The password is the name of narutos first child')
    break
if guess == word:
    print('correct')




"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""


"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""