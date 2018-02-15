# import string
"""import random  # This should be on line 1

print("Hello World")

# Edgar Renteria
# (This is python 2.7)

print(3 + 5)
print(5 - 3)
print(3 * 5)
print(6 / 2)
print(3 ** 2)

# This makes a new line. In phyton 3.6, it looks like: print()
print("see if you can figure this out")
print(20 % 21)

car_name = "Wiebe Mobile"
car_type = "Tesla"
car_cylinders = 8
car_mpg = 9000.1

# Inline printing
print("I have a car called the %s. It's a %s." % (car_name, car_type))


# asking for input
name = input("What is your name? ")  # In phyton 3, it's just called input()
print("Hello %s." % name)

age = input("How old are you? ")
print("%s!? Wow you are older than Jesus." % age)

# Functions


def print_hw():
    print("Hello World")


print_hw()
print_hw()
print_hw()


def say_hi(name):  # name is a parameter
    print("Hello %s." % name)
    print("Enjoy your day.")


say_hi("John")


def print_age(name, age):
    print("%s is %d years old." % (name, age))
    age += 1  # age = age + 1
    print("Next year, they will be %d" % age)


print_age("John", 15)


def f(x):
    return x**3 + 4 * x**2 + 7 * x - 4


print(f(3))
print(f(4))
print(f(5))

# If statement


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    if percentage >= 80:
        return "B"
    if percentage >= 70:
        return "C"
    if percentage >= 60:
        return "D"
    if percentage <= 50:
        return "F"


print(grade_calc(8))


def happy_bday(name):
    print("Happy Birthday to you.")
    print("Happy Birthday to you.")
    print("Happy Birthday dear " + name)
    print("happy Birthday to you.")


happy_bday("John")

# Loops

for num in range(1000000):
    print(num + 1)


#DO NOT RUN!!!
a = 1
while a < 10:
    print(a)
    a += 1


# random numbers

print(random.randint(0, 1001))

# Comparisons
print(1 == 1)  # Is 1 equal to 1?
print(1 != 2)  # is 1 not equal to 2?
print(10 >= 15)
print(not False)

# Recasting

c = '1'
print(c == 1)
print(int(c) == 1)

# Input random ALWAYS gives out a string

# Lists
the_count = [1, 2, 3, 4, 5]
shopping_list = ["Noodles", "Eggrolls", "Milk", "rise", "soda", "chips"]
print(shopping_list[2])
print(len(shopping_list))

# Going through a list
for item in shopping_list:
    print(item)

for num in the_count:
    print(num * 2)

len(shopping_list)  # Gives me a number of the length of the list
range(0)  # Gives a list of the number 0 trough 2
range(len(shopping_list))  # A list of EVERY index in a list

for num in range(len(shopping_list)):
    item = shopping_list[num]
    print("The item at index %d is %s" % (num, item))

# Turn things into a class
str1 = "Hello Class!"
listOne = list(str1)
print(listOne)
listOne[11] = '.'
print(listOne)
print("".join(listOne))

# Add things to a list
shopping_list.append("cereal")
print(shopping_list)

# Removing things from a list
shopping_list.remove("soda")
print(shopping_list)
shopping_list.pop(0)
print(shopping_list)

# the string class
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.punctuation)
print(string.digits)

# Dealing with strings
strTwo = "ThIs iS a VeRY oDd sEnTenCE"
lowercase = strTwo.lower()
print(lowercase)
"""
# Dictionaries - Made up of key: value pairs
dictionary = {'name': 'Lance', 'age': 23, 'height': 5 * 12 + 7}

# access dictionaries
print(dictionary['name'])
print(dictionary['age'])
print(dictionary['height'])

# Adding to a dictionary
dictionary['weight'] = 280
print(dictionary)
larger_dictionary = {
    'CA': [
        'Fresno',
        'sacramento',
        'Los Angeles'
    ],
    'FL': [
        "Tampa",
        "Orlando",
        "Miami"
    ],
    'OH': [
        "Cleveland",
        "Cincinnati",
        "Springfield"
    ]
}
print(larger_dictionary['FL'])
print(larger_dictionary["FL"][2])
print(larger_dictionary['OH'][1])
largest_dictionary = {
    'CA': {
        'NAME': 'California',
        'POPULATION': 39250000,
        'BORDER ST': [
            'Oregon',
            'Nevada',
            'Arizona'
        ]
    },
    'AZ': {
        'NAME': 'Arizona',
        'POPULATION': 6931000,
        'BORDER ST': [
            'California',
            'Utah',
            'Nevada',
            'New Mexico'
        ]
    },
    'NY': {
        'NAME': "New York",
        'POPULATION': 19750000,
        'BORDER ST': [
            'Vermont',
            'Massachusetts',
            'Connecticut',
            'Pennsylvania',
            'New Jersey'
        ]
    }
}

current_node = largest_dictionary['CA']
print(current_node)
print(current_node['NAME'])
print(current_node['POPULATION'])
