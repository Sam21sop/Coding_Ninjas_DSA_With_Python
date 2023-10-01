from sys import setrecursionlimit, stdin
setrecursionlimit(10**6)

def _find_subset_helper(array, start_index, current_subset, result):
    result.append(current_subset[:])
    for i in range(start_index, len(array)):
        current_subset.append(array[i])
        _find_subset_helper(array, i+1, current_subset, result)
        current_subset.pop()

    
def find_subset(array):
    result = []
    _find_subset_helper(array, 0, [], result)
    return result


def take_input():
    n = int(input())
    if n == 0:
        return list()
    return list(map(int, stdin.readline().strip().split()))


def main():
    lst = take_input()
    ans = find_subset(lst)
    for subset in ans:
        print(*subset)


if __name__ == '__main__':
    main()