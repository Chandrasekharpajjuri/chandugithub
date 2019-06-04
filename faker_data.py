from faker import Faker
from random import *
#from random import randint
f=Faker()
n=int(input("How many names do you want:"))
def fake_data(n):
    for i in range(1,n+1):
        print(f.name())
        print(f.city())
        print(f.email())
        print(f.address())
        n=''+str(randint(7,9))
        for i in range(0,9):
            n=n+str(randint(0,9))
        print(n)
        print(f.phone_number())
        print()

from random import *

p=int(input("Enter how many no do you want:"))
def fake_phone(p):
	for i in range(p):
		d=randint(7,9)
		n=''+str(d)
		for i in range(9):
			n=n+str(randint(0,9))
		print(n)
		print()
		#return int(n)
print(phone(p))
"""
from faker import Faker
fake=Faker()
print(fake.name())
"""