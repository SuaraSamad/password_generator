from collections import namedtuple
import datetime

dog = namedtuple('dog',['name','age','breed'])
scoob = dog(name='scooby',age=8,breed='rottweiler')

x = scoob.name
b = scoob.breed
print(x)
print(b)

# creating class with turple

def wish_birthday():
    if datetime.date.today == datetime.date.today:
        print("happy birthday")
    else:
        pass