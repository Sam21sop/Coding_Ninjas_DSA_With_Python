from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)


def getCompressedString(string) :
	# Write your code here.
	i = 0 
	x = ''
	while i < len(string):
		j = i + 1
		c = 1
		while j < len(string) and (string[i] == string[j]):
			j += 1
			c += 1
		if c == 1:
			x += string[i]
		else:
			x += string[i] + str(c)
		i = j
	return x


def main():
    string = stdin.readline().strip();
    ans = getCompressedString(string)
    print(ans)


if __name__ == '__main__':
	main()
	