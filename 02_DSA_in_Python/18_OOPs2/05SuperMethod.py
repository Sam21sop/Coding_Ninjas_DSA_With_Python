class Parent:
    def __init__(self, name):
        self.name = name

    def great(self):
        print(f"Hello I'm {self.name} from the parent class")
    

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def great(self):
        super().great()
        print(f"I'm {self.name} and I'm {self.age} year old.")


def main():
    '''super() is a useful tool for maintaining a clean and structured codebase when working with inheritance in Python.'''
    child_obj = Child('alice', 8)
    child_obj.great()


if __name__ == '__main__':
    main()

'''
Use super() in the constructor of the subclass to ensure proper initialization of the parent class attributes.

Use super() to call methods from the parent class that you want to extend or override in the subclass.

Make sure the method you're calling via super() is defined in the parent class.

super() returns a temporary object of the superclass, which allows you to call its methods as if you're working with the superclass directly.

If you have multiple levels of inheritance, super() automatically handles the hierarchy and calls methods in the correct order. '''