class car:
    manufacture = ""
    model = ""
    year = ""
    price = ""
    has_abs = ""

    def show_details(self):
        print('manufacture is: ' + self.manufacture + ', model is: ' + self.model + ', year  is: ' + str(self.year ) + ', price ? ' + str(self.price))

    def print_abs(self):
        print('has_abs is: ' + str(self.has_abs))


car1 = car()

