from sys import stdin


def stockSpan(price, n) :
	stack = []
	span = [0] * (n)
	for i in range(n):
		while stack and price[stack[-1]] < price[i]:
			stack.pop()
		span[i] = i + 1 if not stack else i - stack[-1]

		stack.append(i)
	return span


def printList(arr) :
	for i in range(len(arr)) :
		print(arr[i], end = " ")
	print()
        

def takeInput():
	size = int(stdin.readline().strip())
	if size == 0 :
		return list(), 0
	price = list(map(int, stdin.readline().strip().split(" ")))
	return price, size


def main():
    price, n = takeInput()
    output = stockSpan(price, n)
    printList(output)


if __name__ == '__main__':
    main()

# n = 8
# price = 60 70 80 100 90 75 80 120
# output = 1 2 3 4 1 1 2 8 