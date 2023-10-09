class Vehical:
    def __init__(self, speed, color) -> None:
        self.color = color
        self.speed = speed

    def show(self):
        print(f"{self.color} {self.speed}")


class Car(Vehical):
    def __init__(self, speed, color) -> None:
        super().__init__(speed, color)


class Bicycle(Vehical):
    def __init__(self, speed, color) -> None:
        super().__init__(speed, color)


def main():
    car = Car(1000, 'red')
    car.show()

if __name__ == '__main__':
    main()