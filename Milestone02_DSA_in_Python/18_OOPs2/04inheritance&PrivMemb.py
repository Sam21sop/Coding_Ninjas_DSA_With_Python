class Parent:
    '''
    it's a good practice to use public members for most interactions and 
    use protected and private members for encapsulation and maintaining a clean interface for your classes.
    '''
    def __init__(self):
        self.public_var = "This is a public variable."
        self._protected_var = "This is a protected variable."
        self.__private_var = "This is a private variable."
        
    def public_method(self):
        print("This is a public method.")

    def _protected_method(self):
        print("This is a protected method.")

    def __private_method(self):
        print("This is a private method.")


class Child(Parent):
    def child_method(self):
        print("This is a method in the child class.")

# Create an instance of the Child class
child_obj = Child()

# Access public members
print(child_obj.public_var)
child_obj.public_method()

# Access protected members (though it's a convention, not enforced)
print(child_obj._protected_var)
child_obj._protected_method()

# Private members cannot be accessed directly (name mangling is applied)
# print(child_obj.__private_var)  # This will result in an error
# child_obj.__private_method()    # This will result in an error

# Access private members using name mangling (not recommended)
print(child_obj._Parent__private_var)
# child_obj._Parent__private_method()
