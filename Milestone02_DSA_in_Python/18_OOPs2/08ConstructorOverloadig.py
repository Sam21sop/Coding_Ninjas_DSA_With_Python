class Student:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age



obj1 = Student('python', 35)
obj2 = Student()

#obj1
print(f'{obj1.name} {obj1.age}')

#obj2
print(f'{obj2.name} {obj2.age}')