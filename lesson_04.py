'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''

x=10
if x >= 10:
    print('True')
else:
    print('False')
'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
age=15
if age < 18:
    print('The price is $10')
else:
    print('It costs $20')

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
my_list=['banana', 'apple', 'strawberry']
y=input('Name a fruit ')

if y in my_list:
    print('Yes thats on my list')
else:
    print('Thats Not on my list')

'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
j=100
k=3
if j == 100 and k == 3:
    print('There is a leap year on this new centery... Thats rare')
'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
cost=input('How much does your order cost per kilogram? $ ')
if cost == str(5) or cost == str(7):
    print('Correct')
elif cost<0:
    print('Error: Invalid spending')
'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''