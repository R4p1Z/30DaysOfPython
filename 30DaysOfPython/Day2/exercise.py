# Day 2: 30 Days of python programming

''' This is a Day 2 exercise 1 for defining variables in Python
I am using multiple lines comment to help reminds the method.
'''

first_name = 'Chawakorn'
last_name = 'Chaimongkol'
full_name = 'Chawakorn Chaimongkol'
country = 'Thailand'
city = 'Nonthaburi'
age = 23
year = 2026
is_married = False
is_true = True
is_light_on = False

#Multiple variables in one line.

is_hungry, pet, dessert = False, 'Kitten', 'Mint Chocolate'

print(pet)

''' This is Day 2 exercise 2 for variables in 30 Days of Python
In this exercise, I will check the data type of all variables and count them using len() function.
'''

print(first_name, type(first_name))
print(last_name, type(last_name))
print(full_name, type(full_name))
print(country, type(country))
print(city, type(city))
print(age, type(age))
print(year, type(year))
print(is_married, type(is_married))
print(is_true, type(is_true))
print(is_light_on, type(is_light_on))
print(is_hungry, type(is_hungry))
print(pet, type(pet))
print(dessert, type(dessert))

len(first_name)
len(last_name)

#Comparing length of first name and last name.
if  len(first_name) > len(last_name):
    print('Length of first name is longer than last name')
else:
    print('Length of last name is longer than first name')    

num_one = 5
num_two = 4
total = num_one + num_two
print(total)

diff = num_two - num_one
print(diff)

product = num_two * num_one
print(product)

division = num_one/num_two
print(division)

remainder = num_two%num_one
print(remainder)

exp = num_one**num_two
print(exp)

floor_division = num_one // num_two
print(floor_division)

#Circle radius & circumference calculation.

radius = 30

area_of_circle = 3.14*(radius**2)
print(area_of_circle)

circum_of_circle = 2*3.14*radius
print(circum_of_circle)

radius = float(input('Area of circle based on '))
area_of_circle = 3.14*(radius**2)
print('is ', area_of_circle)