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

company2 = company
company2.replace('Coding', 'Python')
print(company2)

# Change "Python for Everyone" to "Python for All" using the replace method or other methods.

company2.replace('All', 'Everyone')
print(company2)