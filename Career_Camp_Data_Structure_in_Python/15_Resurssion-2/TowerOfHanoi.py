def tower_of_hanoi(disk, source, aux, dest):
    if disk == 0:
        return 
    if disk == 1:
        print(source, dest)
        return
    tower_of_hanoi(disk-1, source, dest, aux)
    print(source, dest)
    tower_of_hanoi(disk-1, aux, source, dest)


def main():
    num_of_disk = int(input())
    tower_of_hanoi(num_of_disk, 'A', 'B', 'C')


if __name__ == '__main__':
    main()