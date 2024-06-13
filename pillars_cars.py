class car():
    def make_sound(self):
        pass

    def has_wheels(self):
        pass

    def has_engine(self):
        pass

    def is_fast(self):
        pass


class BMW(car):
    def make_sound(self):
        return "after wroom wroom",  'needs repairs'
    

class double_turbo_supra(car):
    def make_sound(self):
        return 'sutututututu',  'engine buzzing'

    
b = BMW()
d = double_turbo_supra()

print(d.make_sound())
print(b.make_sound())