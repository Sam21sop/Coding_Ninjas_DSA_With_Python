def permutation_helper(input_string:str, current:[str], current_visited:[bool], result:[str]):
    if len(current) == len(input_string):
        result.append(current[:])
        return 
    for i in range(len(input_string)):
        if not current_visited[i]:
            current_visited[i] = True
            current.append(input_string[i])
            permutation_helper(input_string, current, current_visited, result)
            current.pop()
            current_visited[i] = False


def permutation(input_string: str):
    result = []
    current_visited = [False] * len(input_string)
    permutation_helper(input_string, [], current_visited, result)
    ans = []
    for sub_str in result:
        ans.append("".join(sub_str))
    return ans
    

def main():
    s = input()
    ans = permutation(s)
    for i in ans:
        print(i)


if __name__ == '__main__':
    main()