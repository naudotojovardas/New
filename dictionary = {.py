contacts = {}

while True :
    action = input('Please choose: Add, Search, Delete, Exit :').lower()
    if action == 'add' :
        name = input('please input a name:') 
        phone = input('Please input a phone number:')
        contacts[name] = phone 
        print('Contact added')
    elif action == 'search' :
        name = input('Please input name:')
        print(f'Name: {contacts.get(name)}')
    elif action == 'delete' :
        name = input('Enter a name:')
        if name in contacts :
            del contacts[name] 
            print('Contact deleted')
        else :
            print('contact not found')
    elif action == 'exit' :
        print('Good bye')
        break
    else:
        print('invalid action try again')

print(f'all contacts:' , contacts)

