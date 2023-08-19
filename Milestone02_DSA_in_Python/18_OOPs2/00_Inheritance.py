class Authentication:
    def __init__(self, first_name, password):
        self.first_name = first_name
        self.password = password

    def show(self):
        print(f'Username: {self.first_name} \nPassword: {self.password}')


class Validation(Authentication):
    def __init__(self):
        super.__init__(self)

    def show(self):
        return super().show()
    

def main():
    # user = Authentication('sopan', 1234)
    valid_user = Validation()


if __name__  == '__main__':
    main()

