print("Welcome to My To-Do Tracker")

with open('projects/to-do.txt') as file:
    list = file.readlines()

while True:
    x=str(input('''Would you like to add or remove an item from your list 
    1 = Add
    2 = Remove
    3 = save and quit
    '''))



    if x == '1':
        list.append(input('What would you like to add? ' + '\n').strip())
    elif x == '2':
        list.remove(input('What would you like to remove? ').strip())
    elif x == '3':
        with open('projects/to-do.txt' , 'w') as file:
            file.writelines(list)
        break
    else:
        print('That is invalid')

    print(list)

    if list == []:
        print('Your list is blank')
