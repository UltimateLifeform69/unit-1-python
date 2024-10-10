contact = dict()



while True:
    x=str(input('''Would you like to add or remove a Contact 
    1 = Add
    2 = Remove
    3 = Show contacts
    '''))



    if x == '1':
        #This is a way to add to Contacts
        contact(input("What is the contact's Name ").strip())
        contact[x](input('What is their phone number ').strip())
    elif x == '2':
        #A way to remove something from Contacts
        y=(input('What would you like to remove? ').strip())
        del y
    elif x == '3':
        #A way to show contacts without changing it
        print(contact)
    else:
        print('That is invalid')
        #Let the user know that there are no other options

    if contact == dict():
        print('Your contacts are empty')