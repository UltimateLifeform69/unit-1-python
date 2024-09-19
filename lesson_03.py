"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
characters=['mario','sonic','cream','luigi']
#made a list
print(characters)
"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
characters.append('yugi')
#Used append to add yugi to the list
print(characters)
"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
characters.remove('cream')
#removed cream
print(characters)
"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
characters[2]= 'ichigo'
print(characters)
"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
characters.append('gojo')
characters.append('goku')
characters.append('bam')
#added more characters
print(characters)
"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
del characters[3]
#Used del to remove 3 from the list
print(characters)

"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
main=characters[0:2]
#made a variable that has a range of 2 people on my list
print(main)
"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
sidechara=['joey','vector','shadow','krillin','robuttnik']
#made a second list with side characters
print(characters+sidechara)
#added both lists together