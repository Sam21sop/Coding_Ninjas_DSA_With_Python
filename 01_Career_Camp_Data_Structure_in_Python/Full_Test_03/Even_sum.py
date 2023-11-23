from sys import stdin

def countWays(array):
    even_count = 0
    odd_count = 0
    for i in range(len(array)):
        if array[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    if odd_count % 2 == 0:
        return even_count
    else:
        return odd_count
    

def main():
    size = int(input())
    arr = list(map(int, stdin.readline().strip().split()))
    result = countWays(arr)
    print(result)

if __name__ == '__main__':
    main()