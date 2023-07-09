def AP(num):
    '''
    series: 3n + 2
    not multiple of 4
    '''
    count = 0
    i = 1
    series_lst = []
    while i <= num + count:
        series = 3 * i + 2
        if series % 4 != 0:
            series_lst.append(series)
        else:
            count += 1
        i += 1
    return series_lst

if __name__ == "__main__":
    number = int(input())
    result = AP(number)
    for i in result:
        print(i, end=' ')