user = 'lukas'
passw = 'lukas123'
new_user = 'gabija'
new_passw = 'desrele'

while True :
    entry = input('enter username :')
    entry1 = input('enter password :') 
    if entry == user and entry1 == passw :
        print(f'Hello, {user}')
        break
    elif entry != user or entry1 != passw : 
        print('F off cunt')
        