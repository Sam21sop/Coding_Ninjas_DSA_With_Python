

def leader_elem(arr):
    current_leader = arr[-1]
    arr = arr[::-1]
    k = [arr[0]]
    for i in range(1, n):
        if arr[i] >= current_leader:
            current_leader = arr[i]
            k.append(arr[i])
    return k


if __name__ == '__main__':

    n = int(input())
    arr = list(map(int, input().split()))
    result = leader_elem(arr)
    print(*result)
