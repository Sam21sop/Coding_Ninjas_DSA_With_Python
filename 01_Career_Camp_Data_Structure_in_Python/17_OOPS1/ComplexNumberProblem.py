class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def plus(self, other):
        self.real = self.real + other.real
        self.imag = self.imag + other.imag

    def multiply(self, other):
        real_part = (self.real * other.real) - (self.imag * other.imag)
        imag_part = (self.real * other.imag) + (self.imag * other.real)
        self.real = real_part
        self.imag = imag_part

    def print(self):
        print('{0} + i{1}'.format(self.real, self.imag))


def main():
    c1 = [int(elem) for elem in list(input().strip().split())]
    c2 = [int(elem) for elem in list(input().strip().split())]
    
    com1 = ComplexNumber(c1[0], c1[1])
    com2 = ComplexNumber(c2[0], c2[1])
    choice = int(input())
    if choice == 1:
        com1.plus(com2)
        com1.print()
    elif choice == 2:
        com1.multiply(com2)
        com1.print()


if __name__ == '__main__':
    main()