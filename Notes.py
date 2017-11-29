# print("Hello World")
#
# # Edgar Renteria
# # (This is python 2.7)
#
# print(3 + 5)
# print(5 - 3)
# print(3 * 5)
# print(6 / 2)
# print(3 ** 2)
#
# # This makes a new line. In phyton 3.6, it looks like: print()
# print("see if you can figure this out")
# print(20 % 21)
#
# car_name = "Wiebe Mobile"
# car_type = "Tesla"
# car_cylinders = 8
# car_mpg = 9000.1
#
# # Inline printing
# print("I have a car called the %s. It's a %s." % (car_name, car_type))
#
#
# # asking for input
# name = input("What is your name? ")  # In phyton 3, it's just called input()
# print("Hello %s." % name)
#
# age = input("How old are you? ")
# print("%s!? Wow you are older than Jesus." % age)

# Functions


def print_hw():
    print("Hello World")


print_hw()
print_hw()
print_hw()


def say_hi(name):  # name is a parameter
    print("Hello %s." % name)
    print("Enjoy your day.")


say_hi("john")


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
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


print(grade_calc(8))
