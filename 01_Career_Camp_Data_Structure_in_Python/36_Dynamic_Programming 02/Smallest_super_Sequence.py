from sys import stdin

def smallestSuperSequence(str1:str, str2:str):
    str1_size = len(str1)
    str2_size = len(str2)

    subproblem_memo = [[0] * (str2_size + 1) for _ in range(str1_size + 1)]

    for i in range(str1_size + 1):
        for j in range(str2_size + 1):
            if i == 0:
                subproblem_memo[i][j] = j
            elif j == 0:
                subproblem_memo[i][j] = i
            elif str1[i-1] == str2[j-1]:
                subproblem_memo[i][j] = 1 + subproblem_memo[i-1][j-1]
            else:
                subproblem_memo[i][j] = 1 + min(subproblem_memo[i-1][j], subproblem_memo[i][j-1])
    return subproblem_memo[str1_size][str2_size]


def take_input():
    str1 = input().strip()
    str2 = input().strip()
    return str1, str2


def main():
    s1, s2 = take_input()
    res = smallestSuperSequence(s1, s2)
    print(res)

if __name__ == '__main__':
    main()