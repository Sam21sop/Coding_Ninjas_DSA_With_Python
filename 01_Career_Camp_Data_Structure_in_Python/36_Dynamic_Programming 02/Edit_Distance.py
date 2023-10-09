from sys import stdin

def edit_distnace_helper(string1, string2, subproblem):
    if len(string1) == 0:
        return len(string1)
    if len(string2) == 0:
        return len(string2)
    
    str1_size = len(string1)
    str2_size = len(string2)
    
    if subproblem[str1_size][str2_size] != -1:
        return subproblem[str1_size][str2_size]

    if string1[0] == string2[0]:
        small_ans = edit_distnace_helper(string1[1:], string2[1:], subproblem)
        subproblem[str1_size-1][str2_size-1] = small_ans
        subproblem[str1_size][str2_size] = 0 + small_ans
    else:
        remove = edit_distnace_helper(string1[1:], string2, subproblem)
        subproblem[str1_size-1][str2_size] = remove

        insert = edit_distnace_helper(string1, string2[1:], subproblem)
        subproblem[str1_size][str2_size-1] = insert

        substitute = edit_distnace_helper(string1[1:], string2[1:], subproblem)
        subproblem[str1_size-1][str2_size-1] = substitute

        subproblem[str1_size][str2_size] = 1 + min(remove, insert, substitute)
    return subproblem[str1_size][str2_size]


def edit_distance(str1, str2):
    str1_size = len(str1)
    str2_size = len(str2)
    subproblem =  [[-1] * (str2_size+1) for _ in range(str1_size+1)]
    return edit_distnace_helper(str1, str2, subproblem)


def main():
    s1 = input()
    s2 = input()
    res = edit_distance(s1, s2)
    print(res)

main()