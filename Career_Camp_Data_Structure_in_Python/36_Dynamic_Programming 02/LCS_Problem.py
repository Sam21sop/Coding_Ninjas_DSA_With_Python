from sys import stdin

def LCS(string1:str, string2:str):
    length_str1 = len(string1)
    length_str2 = len(string2)
    sub_problem_memo = [[0] * (length_str2+10) for _ in range(length_str1+10)]

    for curr_start in range(1, length_str1 + 1):
        for curr_end in range(1, length_str2 + 1):
            if string1[length_str1 - curr_start] == string2[length_str2 - curr_end]:
                sub_problem_memo[curr_start][curr_end] = 1 + sub_problem_memo[curr_start-1][curr_end-1]
            else:
                sub_problem_memo[curr_start][curr_end] = max(sub_problem_memo[curr_start-1][curr_end], sub_problem_memo[curr_start][curr_end-1])

    return sub_problem_memo[length_str1][length_str2]


def main():
    s1 = str(stdin.readline().strip())
    s2 = str(stdin.readline().strip())
    res = LCS(s1, s2)
    print(res)

if __name__ == '__main__':
    main()