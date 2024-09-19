"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""
word=input('Type your password: ').lower()
#Used lower to make it not be case sensitive
pas='yeet'
if word==pas:
    print('correct')
else:
    print('incorrect')
#if statement to state if the password was correct or not.
"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
space=input('Type something').strip()
#Used strip to make any spaces invalid
if space=="":
    print('invalid')
else:
    print("Valid")
#Made nothing invalid and everything else valid
"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
anny="cat"
new_anny=anny.replace('cat','dog').lower()
#used replace to chage cat into dog
print(new_anny)

"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
name=input('what is your name? ')
age=input('how old are you? ')
sentence=f'your name is {name} and you are {age} years old.'
#Used the f'' format because it is the perfect way to do it.
print(sentence)


"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)

"""
flt=2.5
flt2=5.5
ans=flt2/flt
print(f'{flt}/{flt2}={ans:.1f}')