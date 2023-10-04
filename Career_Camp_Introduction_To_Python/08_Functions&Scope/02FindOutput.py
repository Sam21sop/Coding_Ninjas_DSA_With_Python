def find_output(n, r):
    factn = factr = factnr = 1
    for i in range(2, n+1):
        factn *= i
        if i <= r:
            factr *= i
        if i <= n-r:
            factnr *= i 
    ncr = int(factn / (factnr * factr))
    return ncr 

if __name__ == "__main__":
    n = 10
    r = 6
    result = find_output(n, r)
    print(result)

