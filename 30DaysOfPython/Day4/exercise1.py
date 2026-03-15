# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

'''a, b, c, d , space = 'Thirty', 'Days', 'Of', 'Python', ' '
print(f'{a} {b} {c} {d}')'''

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

"""word = ['Coding', 'For', 'All']
result = ' '.join(word)
print(result)"""

# Declare a variable named company and assign it to an initial value "Coding For All".

company = "Coding For All"
first_word = company.split()
#print(first_word[0])

# Print the variable company using print().

#print(company)

# Print the length of the company string using len() method and print().

#print(len(company))

# Change all the characters to uppercase letters using upper() method.

#print(company.upper())

# Change all the characters to lowercase letters using lower() method.

#print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

'''print(company.capitalize())
print(company.title())
print(company.swapcase())'''

# Cut(slice) out the first word of Coding For All string.

'''first_word = company[:6]
print(first_word)'''

# Check if Coding For All string contains a word Coding using the method index, find or other methods.

# print('Coding' in company) # 1st method
'''substring1 = 'Coding'
print(company.index(substring1))'''

# Replace the word coding in the string 'Coding For All' to Python.

'''company2 = company.replace('Coding', 'Python')
print(company2)'''

# Change "Python for Everyone" to "Python for All" using the replace method or other methods.

'''company3 = company2.replace('All', 'Everyone')
print(company3)'''

# Split the string 'Coding For All' using space as the separator (split()) .

'''print(company.split())'''

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

'''big_tech = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(big_tech.split(', '))'''

# What is the character at index 0 in the string Coding For All.

'''print(company[0])''' # It's "C"

# What is the last index of the string Coding For All.

'''print(company[-1])''' # It's "l"

# What character is at index 10 in "Coding For All" string.

'''print(company[10])''' # It's a space

# Create an acronym or an abbreviation for the name 'Python For Everyone'.

'''word1 = "Python For Everyone"
acronym1 = ''.join(word[0].upper() for word in word1.split())
print(acronym1)'''

# Create an acronym or an abbreviation for the name 'Coding For All'.

'''word2 = 'Coding For All'
acronym2 = ''.join(word[0].upper() for word in word2.split())
print(acronym2)'''

# Use index to determine the position of the first occurrence of C in Coding For All.

'''print(company.index('C'))'''

# Use index to determine the position of the first occurrence of F in Coding For All.

'''print(company.index('F'))'''

# Use rfind to determine the position of the last occurrence of l in Coding For All People.

'''print(company.rfind('l'))'''

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

'''word3 = 'You cannot end a sentence with because because because is a conjunction'
print(word3.find("because"))
print(word3.index("because"))'''

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

word4 = 'You cannot end a sentence with because because because is a conjunction'
'''print(word4.rindex("because"))'''

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

'''print(word4[word4.index("because"):word4.rindex("e")+1])
'''

# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
'''
print(word4.index("because"))'''

# Does 'Coding For All' start with a substring Coding?

'''word5 = company.split()
print(word5[0])
print(word5[0] == 'Coding')

print(company.startswith("Coding"))
'''
# Does 'Coding For All' end with a substring coding?

'''print(word5[-1])
print(word5[-1] == 'coding')

print(company.endswith("coding"))
'''
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.

"""word6 = '   Coding For All      '
print(word6.strip('   '))"""

# Which one of the following variables return True when we use the method isidentifier():
# - 30DaysOfPython
# - thirty_days_of_python
'''
a = "30DaysOfPython"
b = "thirty_days_of_python"

print(a.isidentifier())
print(b.isidentifier())'''

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
'''
lib1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
separator = " # "
print("#", separator.join(lib1))'''

# Use the new line escape sequence to separate the following sentences.
"""I am enjoying this challenge.
I just wonder what is next."""
'''
print(
    "I am enjoying this challenge. \nI just wonder what is next."
)'''

# Use a tab escape sequence to write the following lines.
'''
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")'''

# Use the string formatting method to display the following:
'''
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square.')'''

# Make the following using string formatting methods:

x = 8
y = 6

print(f"{x} + {y} = {x+y}")
print(f"{x} - {y} = {x-y}")
print(f"{x} * {y} = {x*y}")
print(f"{x} / {y} = {x/y:.2f}")
print(f"{x} % {y} = {x%y}")
print(f"{x} // {y} = {x//y}")
print(f"{x} ** {y} = {x**y}")