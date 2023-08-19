class Vehical:
    def __init__(self) -> None:
        self.color = None
        self.__number = None

    def set_number(self, number):
        number = number

    def get_number(self):
        return self.__number 


class Car(Vehical):
    def main(self):
        v = Vehical()
        v.color = 'White'
        v.set_number(1010)
        print(v.color, v.get_number())

c = Car()
c.main()
