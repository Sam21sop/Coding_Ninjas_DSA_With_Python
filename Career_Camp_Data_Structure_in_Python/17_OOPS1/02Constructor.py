class Student:
    def __init__(self, name:str, course:str):
        self.name = name
        self.course = course

    def show(self):
        print(self.name, self.course)

std1 = Student('Sopan', 'AIML')
std1.show()