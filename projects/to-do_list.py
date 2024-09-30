print("Welcome to My To-Do Tracker")
#stt the text file as my list
with open('projects/to-do.txt') as file:
    list = file.readlines()
#Stared an infinate loop
while True:
    x=str(input('''Would you like to add or remove an item from your list 
    1 = Add
    2 = Remove
    3 = save and quit
    '''))



    if x == '1':
        #This is a way to add to the list
        list.append(input('What would you like to add? ' + '\n').strip())
    elif x == '2':
        #A way to remove something from the list
        list.remove(input('What would you like to remove? ').strip())
    elif x == '3':
        #A way to stop the program (save and quit)
        with open('projects/to-do.txt' , 'w') as file:
            file.writelines(list)
        break
        #A way to stop the code completely
    else:
        print('That is invalid')
        #Let the user
    print(list)

    if list == []:
        print('Your list is blank')
