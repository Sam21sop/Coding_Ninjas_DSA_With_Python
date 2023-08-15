class Person:
    def __init__(self):
        self.name = None
        self.weight = None


class Student(Person):
    def __init__(self):
        super().__init__()
        self.roll_number = None
        self.school_name = None

    def show(self):
        print(f'{self.roll_number} {self.name} {self.weight}')



def main():
    s= Student()
    s.name = 'Ayush'
    s.roll_number = 10
    s.weight = 65
    s.school_name = "Vijaya Sr. Sec. School"
    s.show()

if __name__ == '__main__':
    main()