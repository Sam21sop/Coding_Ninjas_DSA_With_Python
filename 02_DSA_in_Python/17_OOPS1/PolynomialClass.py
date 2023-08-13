class Polynomial:
    def __init__(self):
        self.coefficients = {}


    def setCoefficient(self, degree, coefficient):
        self.coefficients[degree] = coefficient


    def add(self, poly):
        result = Polynomial()
        for degree, coefficient in self.coefficients.items():
            result.setCoefficient(degree, coefficient)
        for degree, coefficient in poly.coefficients.items():
            if degree in result.coefficients:
                result.coefficients[degree] += coefficient
            else:
                result.setCoefficient(degree, coefficient)
        return result


    def subtract(self, poly):
        result = Polynomial()
        for degree, coefficient in self.coefficients.items():
            result.setCoefficient(degree, coefficient)
        for degree, coefficient in poly.coefficients.items():
            if degree in result.coefficients:
                result.coefficients[degree] -= coefficient
            else:
                result.setCoefficient(degree, -coefficient)
        return result


    def multiply(self, poly):
        result = Polynomial()
        for deg1, coef1 in self.coefficients.items():
            for deg2, coef2 in poly.coefficients.items():
                degree = deg1 + deg2
                coefficient = coef1 * coef2
                if degree in result.coefficients:
                    result.coefficients[degree] += coefficient
                else:
                    result.setCoefficient(degree, coefficient)
        return result


    def print1(self):
        sorted_degrees = sorted(self.coefficients.keys())
        terms = []
        for degree in sorted_degrees:
            coefficient = self.coefficients[degree]
            if coefficient != 0:
                # term = "{0}x^{1}".format(coefficient, degree)
                term = "{0}x{1}".format(coefficient, degree)
                terms.append(term)
        if len(terms) > 0:
            # print(" + ".join(terms))
            print(" ".join(terms))
        else:
            print("0")


def main():
    n1 = int(input())
    degrees1 = list(map(int, input().split()))
    coefficients1 = list(map(int, input().split()))

    n2 = int(input())
    degrees2 = list(map(int, input().split()))
    coefficients2 = list(map(int, input().split()))

    choice = int(input())

    # Creating Polynomial objects
    poly1 = Polynomial()
    for degree, coefficient in zip(degrees1, coefficients1):
        poly1.setCoefficient(degree, coefficient)

    poly2 = Polynomial()
    for degree, coefficient in zip(degrees2, coefficients2):
        poly2.setCoefficient(degree, coefficient)

    # Performing the desired operation based on the choice
    if choice == 1:
        result = poly1.add(poly2)
        result.print1()
    elif choice == 2:
        result = poly1.subtract(poly2)
        result.print1()
    elif choice == 3:
        result = poly1.multiply(poly2)
        result.print1()


if __name__ == '__main__':
    main()


# 3
# 3 1 7
# 1 2 3
# 2
# 2 1
# 7 8
# 3