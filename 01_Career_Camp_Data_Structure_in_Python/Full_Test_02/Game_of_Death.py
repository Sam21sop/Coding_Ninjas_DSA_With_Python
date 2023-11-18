def findLastPersonToSurvive(num, k):
    people = list(range(1, num+1))
    current_position = 0
    while len(people) > 1:
        current_position = (current_position + k - 1) % len(people)
        del people[current_position]
    return people[0]


def main():
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    last_person = findLastPersonToSurvive(n, k)
    print(last_person)

if __name__ == '__main__':
    main()