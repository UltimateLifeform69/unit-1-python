'''
Welcome to the Calculatinator-inator 9000!

Enter the first number: 10
Enter the second number: 5

Select operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Floor Division
6. Exponential
7. Remainder

Enter choice: 3

Result: 50.0
'''

print('WELCOME TO A PYTHON CALCULATOR')

x=float(input('Give me a number '))
y=float(input('Give me another number '))
z=input('''Select operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Floor Division
6. Exponential
7. Remainder?
    ''')
#Gave the user options
if z=="Addition":
    print(x+y)
elif z=="Subtraction":
    print(x-y)
elif z=="Multiplication":
    print(x*y)
elif z=="Division":
    print(x/y)
elif z=="Floor Division":
    print(x//y)
elif z=="Exponetial":
    print(x**y)
elif z=="Remainder":
    print(x%y)
else:
    print('invalid')
    #Made an elif for every equation based on the user's choice

