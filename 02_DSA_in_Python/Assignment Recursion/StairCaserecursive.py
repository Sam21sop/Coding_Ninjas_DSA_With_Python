def staircase_ways(number):
    if number < 3:
        return number
    elif number == 3:
        return 4
    else:
        return staircase_ways(number-1) + staircase_ways(number-2) + staircase_ways(number-3)
    

def main():
    num = int(input())
    ways = staircase_ways(num)
    print(ways)


if __name__ == "__main__":
    main()