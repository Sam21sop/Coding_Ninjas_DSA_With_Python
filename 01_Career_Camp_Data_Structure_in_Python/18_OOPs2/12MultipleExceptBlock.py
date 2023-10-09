print('Execution started Normally')
lst = [10, 20, 0, 3, 5]
dictionary = {1:'Python', 2:'C', 3:'JavaScript', 4:'Java'}

try:
    rank = int(input('Enter rank: '))
    print(dictionary[rank])
    numerator = int(input('Enter the numerator index: '))
    denominator = int(input('Enter the denominator index: '))
    print(lst[numerator] / lst[denominator])
except KeyError as e:
    print(e)
except IndexError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)

print('Execution terminated normally.')
