# Defining a class
class Shoes(object):
    def __init__(self, lace_color, lighting, brand):  # TWO underscore before and after init
        # Things a shoe has
        self.lace_color = lace_color
        self.rgb_lighting = lighting
        self.used = False
        self.brand = brand
        self.clean = True

    def wear(self):
        self.used = True
        self.clean = False
        print("You wear the shoes")

    def wash(self):
        self.clean = True
        print("You clean the shoes")


first_pair = Shoes("Red", True, "Jordan")
second_pair = Shoes("Pink", False, "Sketchers")

print(first_pair.brand)
print(second_pair.lace_color)
print(first_pair.clean)

first_pair.wear()
print(first_pair.clean)
first_pair.wash()
print(first_pair.clean)


class Car(object):
    def __init__(self, color, name, model, horsepower, passenger):
        self.name = name
        self.color = color
        self.model = model
        self.hp = horsepower
        self.passenger = passenger
        self.running = False

    def driving_forward(self):
        if self.running:
            print("You move forward")
        else:
            print("Nothing Happens.")

    def turn_on(self):
        if self.running:
            print("Nothing Happens")
        else:
            self.running = True
            print("You start the car")

    def turn_off(self):
        if self.running:
            self.running = False
            print("You have stopped")
        else:
            print("Nothing happens")

    def go_for_drive(self, passengers):
        print("%d passengers get in" % passengers)
        self.passenger = passengers
        self.turn_on()
        self.driving_forward()
        self.driving_forward()
        self.driving_forward()
        self.turn_off()
        print("%d passengers get out" % passengers)
        self.passenger = 0


my_car = Car("Red", "Tesla", "X", 9001, 0)
my_car.go_for_drive(4)
