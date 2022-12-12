from collections import namedtuple

dog = namedtuple('dog',['name','age','breed'])
scoob = dog(name='scooby',age=8,breed='rottweiler')

x = scoob.name
b = scoob.breed
print(x)
print(b)