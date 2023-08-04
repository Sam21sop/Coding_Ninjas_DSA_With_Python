def pair_star(strings):
    if len(strings) <= 1:
        return strings
    if strings[0] != strings[1]:
        return strings[0] + pair_star(strings[1:])
    else:
        return strings[0] + "*" + pair_star(strings[1:])
    

def main():
    s = input().strip()
    result = pair_star(s)
    print(result)


if __name__ == '__main__':
    main()