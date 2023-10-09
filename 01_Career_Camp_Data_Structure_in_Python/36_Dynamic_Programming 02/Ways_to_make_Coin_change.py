from sys import stdin

def ways_to_coin_make_change(denomination:[int], num_of_denomination:int, values:int):
    sub_problem_memo = [0] * (values+1)
    sub_problem_memo[0] = 1
    for coin in denomination:
        for val in range(coin, values+1):
            sub_problem_memo[val] += sub_problem_memo[val-coin]
    return sub_problem_memo[values]


def main():
    numDenominations = int(stdin.readline().rstrip())
    denominations = [int(elem) for elem in list(stdin.readline().rstrip().rsplit())]
    value = int(input().strip())
    res = ways_to_coin_make_change(denominations,numDenominations, value)
    print(res)

if __name__ == '__main__':
    main()