from collections import deque

def _dfsHelper(x, num):
    q = deque()
    q.append(num)
    while q:
        num = q.popleft()
        if num <= x:
            print(num, end=' ')
            last = num % 10
            if last == 0:
                q.append((num * 10) + (last + 1))
            elif last == 9:
                q.append((num * 10) + (last - 1))
            else:
                q.append((num * 10) + (last + 1))
                q.append((num * 10) + (last - 1))

def showJumpingNum(x):
    print('0', end=' ')
    for i in range(1, 10):
        _dfsHelper(x, i)

def main():
    n = int(input())
    showJumpingNum(n)

if __name__ == '__main__':
    main()
