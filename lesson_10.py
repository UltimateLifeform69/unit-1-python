from datetime import datetime
from datetime import date
from datetime import time

"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
today = datetime.now()
print(today)

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
uk = today.strftime("%m/%d/%Y")
print(uk)
"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
y='2024/10/05'

z='2024/10/02'

y2=(datetime.strptime(y, '%Y/%m/%d' ))
z2=(datetime.strptime(z, '%Y/%m/%d' ))

print(y2-z2)

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
