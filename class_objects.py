# write a program to create a class and object to demonstrate calling method in python
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display_info(self):
        print(f'Name: {self.name}, Age: {self.age}, City: {self.city}')


class car:
    def start(self):
        print("The car engine has started!")

    def stop(self):
        print("The car engine has stopped!")


c1 = car()
c1.start()
c1.stop()

# write a program to use constructor to initialize data and destructor to clean up the data in python


class demo:
    def __init__(self, data):
        self.data = data
        print(f'Object created with data: {self.data}')

    def __del__(self):
        print(f'Object with data: {self.data} is being destroyed')


d = demo("Sample Data")
del d
