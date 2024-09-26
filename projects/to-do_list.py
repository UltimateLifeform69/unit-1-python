print("Welcome to My To-Do Tracker")

list=[]

while True:
    x=str(input('''Would you like to add or remove an item from your list 
    1 = Add
    2 = Remove
    '''))



    if x == '1':
        list.append(input('What would you like to add? ').strip())
    elif x == '2':
        list.remove(input('What would you like to remove? ').strip())
    else:
        print('That is invalid')

    print(list)

    if list == []:
        print('Your list is blank')
