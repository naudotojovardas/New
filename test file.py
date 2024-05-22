ask = input('Hello, are you a member? : ')
yes = 'yes'
no = 'no'
age = '12'

if ask == yes :
    age1 = input('How old are you? : ')
if age > age1 :
        ask1 = input('Is anyone acompaning you? : ')
        if ask1 == yes :
            print('You can loan books')
        else : 
            print('you can only loan children books')
if age < age1 : 
    print('you can loan books')


