#!/usr/bin/env python3

import builtins


print("Hello Python interpreter!")
message = "go outdoor"
print(message)

first_name ='john'
last_name = 'wick'
full_name=f"{first_name} {last_name}"
print(full_name)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.append('giant')

print(bicycles)
bicycles.sort()
print(bicycles)
for x in bicycles:
    print(x)
sum=0
for x in range(1,3):
    sum += x
print(sum)

for bike in bicycles:
    if bike == 'trek':
        print(bike.upper())
    else:
        print(bike)

available_toppings = ['mushrooms','olives','green peppers']
requested_toppings = ['extra cheese','mushrooms']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}")
print("\nFinished making your pizza!")

alien = {}
alien['color']='green'
print(alien)


users = {
     'aeinstein': {
         'first': 'albert',
         'last': 'einstein',
         'location': 'princeton',
         },
     'mcurie': {
         'first': 'marie',
         'last': 'curie',
         'location': 'paris',
         },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

def build_person(first,last):
    """Retrun a dic"""
    person = {'first': first, 'last': last}
    return person
musician = build_person('Jimmy', 'Hendrix')
print(f"\n{musician}")
