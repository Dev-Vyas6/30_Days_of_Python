# variables in Python

first_name = 'Dev'
last_name = 'Vyas'
country = 'India'
city = 'Bardoli'
age = 19
is_married = False
skills = ['HTML','CSS','JS','Python']
person_info = {
    'firstname':'Dev', 
    'lastname':'Vyas', 
    'country':'India',
    'city':'Bardoli'
    }

# Printing the alues stored in the Variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Dev', 'Vyas', 'Bardoli', 19, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
