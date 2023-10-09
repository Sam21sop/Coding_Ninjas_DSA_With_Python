from math import sqrt
#
def minimum_count(number):
    if number <= 0:
        return 0
    min_count = [float('inf')] * (number+1)
    min_count[0] = 0
    for i in range(1, int(sqrt(number))+1):
        for j in range(i*i, number+1):
            min_count[j] = min(min_count[j], min_count[j-i*i] + 1)
    return min_count[number]


def main():
    num = int(input())
    result = minimum_count(num)
    print(result)



if __name__ == '__main__':
    main()