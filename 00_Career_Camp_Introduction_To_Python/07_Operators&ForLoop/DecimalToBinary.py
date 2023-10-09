def decToBin(number):
    binary = bin(number)[2:]
    return binary

if __name__ == "__main__":
    num = int(input())
    result = decToBin(num)
    print(result)