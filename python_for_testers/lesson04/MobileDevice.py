class MobileDevice:
    def __init__(self, model, os, version, has_flash, price, screen_width, screen_height):
        self.model = model
        self.os = os
        self.version = version
        self.has_flash = has_flash
        self.price = price
        self.screen_width = screen_width
        self.screen_height = screen_height
        if screen_width < 0:
            screen_width = screen_width * -1
            self.screen_width = screen_width
            print("Screen width was a negative number and changed")
        if screen_height < 0:
            screen_height = screen_width * -1
            self.screen_height = screen_width
            print("Screen height was a negative number and changed")

    def print_parameters(self):
        print("Model:" + self.model + ", os:" + self.os + ", version:" + str(self.version) + ", has flash:" + str(
            self.has_flash) + ", prics:" + str(self.price))

    def calc_screen_area(self):
        return self.screen_width * self.screen_height

    def picture_quality(self):
        if self.has_flash:
            print('Good Quality')
        else:
            print('Bad Quality')


device1 = MobileDevice('iphone Pro max', 'ios', 14.3, True, 5000, 10.2, 9.8)
device1.print_parameters()
print(device1.calc_screen_area())
device1.picture_quality()

device2 = MobileDevice('iphone x', 'ios', 14.1, True, 5000, 14.2, 10.3)

device2.print_parameters()
print(device2.calc_screen_area())
device2.picture_quality()


# Q4
class Family:
    family_name = 'Dadon'


class Child1(Family):
    my_name = 'Dolev'


class Child2(Family):
    my_brother = 'Amit'


child1 = Child1()
print(child1.my_name + " " + child1.family_name)

child2 = Child2()
print((child2.my_brother + " " + child2.family_name))