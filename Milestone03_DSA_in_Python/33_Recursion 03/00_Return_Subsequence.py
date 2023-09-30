def subequence(input_str):
    if len(input_str) == 0:
        output = ''
        return output
    small_output = subequence(input_str[1:])
    output = str(small_output)  * 2
    for i in range(len(small_output)):
        output[i] = small_output[i]
    for i in range(len(small_output)):
        output[i] = input_str[0] + small_output[i]


def main():
    s = input()
    res = subequence(s)
    print(res)


main()