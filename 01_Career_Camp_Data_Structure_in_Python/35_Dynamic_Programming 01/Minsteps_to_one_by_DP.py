from sys import stdin, maxsize as MAX_VALUE


def minsteps_to_one(num):
    if num == 1:
        return 0
    min_step = [0] * (num + 1)
    min_step[1] = 0

    for curr_step in range(2, num+1):
        subtract_by_one = min_step[curr_step - 1]
        divided_by_two = MAX_VALUE
        divided_by_three = MAX_VALUE
        if curr_step % 2 == 0:
            divided_by_two = minsteps_to_one(num // 2)
        if curr_step % 3 == 0:
            divided_by_three = minsteps_to_one(num // 3)
        min_step[curr_step] = 1 + min(subtract_by_one, divided_by_two, divided_by_three)
    return min_step[num]


def main():
    num = int(stdin.readline().strip()) 
    res = minsteps_to_one(num)
    print(res)


if __name__ == "__main__":
    main()