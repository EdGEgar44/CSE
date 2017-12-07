# 12.4.17


def reverse_order(last_name, first_name):
    print("%s, %s" % (last_name, first_name))


reverse_order("Lopez", "Gorge")

# 12.5.17


def add_py(name):
    print("%s.py" % name)  # Solution 1
    print(name + ".py")  # Solution 2


add_py("name")

# 12.6.17


def add(number, number2, number3):
    print(number + number2 + number3)


add(6, 3, 5)

# 12.7.17


def repeat(string):
    # or print(string)
    # or print(string)
    # and print(string)
    for x in range(1):
        print(string)


repeat("Hello.")

# 12.8.17
