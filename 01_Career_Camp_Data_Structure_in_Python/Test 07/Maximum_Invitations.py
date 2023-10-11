def peri(w, h):
    return (w * 2) + (h * 2)

def maximum_invitations():
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    count = [0] * m
    max_area = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '.':
                count[j] += 1
            else:
                count[j] = 0
        for j in range(m):
            h = count[j]
            w = 1
            if h > 0:
                k = j + 1
                while k < m and count[k] >= h:
                    w += 1
                    k += 1
                k = j - 1
                while k >= 0 and count[k] >= h:
                    w += 1
                    k -= 1
            max_area = max(max_area, peri(w, h))
    print(max_area - 1)


maximum_invitations()