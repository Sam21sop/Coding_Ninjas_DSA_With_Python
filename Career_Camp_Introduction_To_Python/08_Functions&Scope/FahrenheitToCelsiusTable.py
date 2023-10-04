def print_table(start, stop, step):
    '''Function print the Fahrenheit to Celsius Table'''
    for f in range(start, stop+1, step):
        print(f, int((f-32) * 5/9))


if __name__ == '__main__':
    start = int(input())
    stop = int(input())
    step = int(input())
    print_table(start, stop, step)