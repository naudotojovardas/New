class InvalidAgeError(Exception):
    def __init__(self, age, message):
        self.age = age
        self.message = message

    def verification(self, age, min_age=18):
        if age < min_age:
            raise InvalidAgeError('no, no, no u naughty, naughty:)')
        else:
            print('Hello my friend')
        return 'You In'


I = InvalidAgeError(Exception)     
print(I.verification(19))
        


        
