class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


obj = Person('python', 35)
print('Language Name:', obj.name, 'Age:', obj.age)
