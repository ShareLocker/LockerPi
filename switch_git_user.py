import os

name = input('git email: ')
os.system('git config user.email "{}"'.format(name))

name = input('name: ')
os.system('git config user.name "{}"'.format(name))
