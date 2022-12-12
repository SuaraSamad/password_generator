class dog():
    
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + ' says hello!'


class cat():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + ' says hello!'

gadafi = dog('gadafi')
scooby = cat('scooby')


def pet_speak(pet):
    print(pet.speak())


class animal():
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError('class must implement this abstract method')

class dogg(animal):
    def speak(self):
        print(self.name + 'says HELLO!')

class catt(animal):
    def speak(self):
        print(self.name + ' says HELLO!')

gad = dogg('gad')
scob = catt('scob')

print(gad.speak())