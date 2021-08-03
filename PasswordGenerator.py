import random
passlen = int(input('Enter password length'))
s = 'abcdefghijklmnopqrstuvxwyz0123456789ABCDEFGHIJKLMNOPQRSTUVXWYZ!@#$%^&*()'
p = "".join(random.sample(s,passlen))
print(p)