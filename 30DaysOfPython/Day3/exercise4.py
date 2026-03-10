'''x = float(input('Enter the number: '))
y =  x%2

if (y > 0):
    print('This is an odd number', x, y)
else:
    print('This is an even number.', x, y)

print(7//3 == int(2.7))

print(type('10') == 10)

print(int(9.8) == 10)'''

# Weekly salary calculation

'''work_hours = int(input('Enter hours: '))
rate_per_hour = int(input('Enter rate per hour: '))
print("Your weekly earning is", work_hours*rate_per_hour)
'''
# Years a person can live in seconds

'''years = int(input('Enter number of years you have lived: '))
years_in_seconds = years*365*24*60*60
print("You have lived for", years_in_seconds, "seconds.")'''

# Python script to generates table of numbers based on input

num = int(input("Enter your number: "))
x = 1

while(x!=(num+1)):
    print(x, x**0, x**1, x**2, x**3)
    x += 1