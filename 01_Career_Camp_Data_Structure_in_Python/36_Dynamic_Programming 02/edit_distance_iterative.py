
from sys import stdin


def editDistance(s, t) :
	m = len(s)
	n = len(t)

	#create 2D matrics to store the edit distance
	dp = [[0]*(n+1) for _ in range(m+1)]

	#initialize the base case
	for i in range(m+1):
		dp[i][0] = i
	for j in range(n+1):
		dp[0][j] = j

	#fill in the rest of the matrix
	for i in range(1, m+1):
		for j in range(1, n+1):
			if s[i-1] == t[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

	return dp[m][n]


#main
s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())

print(editDistance(s, t))