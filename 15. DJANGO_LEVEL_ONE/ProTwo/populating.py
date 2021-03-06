import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

from AppTwo.models import User
from faker import Faker

fakergen = Faker()

def populate(N = 5):

    for entry in range(N):
        name = fakergen.name().split()
        first_name = name[0]
        last_name = name[1]
        email = fakergen.email()
        userModel = User.objects.get_or_create(first_name = first_name, last_name = last_name, email = email)

if __name__ == '__main__' :
    print('population Script is running')
    populate(20)
    print('population complete')