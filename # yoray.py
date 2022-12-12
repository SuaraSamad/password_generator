# password generator
import random
import math

def set_password():
     random.seed(42)
     passwordL = 'abcdefghijklmnopqrstuvwxyz1234567890'
     mypassword = random.choices(population = passwordL,k = 10)
     print(mypassword)
set_password()

