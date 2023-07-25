from sys import stdin

# def isPermutation(string1, string2):
#     if len(string1) != len(string2):
#         return False
#     frequency = [0] * 256
#     for i in range(len(string1)):
#         ch = ord(string1[i])
#         frequency[ch] += 1
#     for i in range(len(string2)):
#         ch = ord(string2[i])
#         frequency[ch] -= 1
#     for i in range(256):
#         if frequency[i] != 0:
#             return False
#     return True

def isPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False


def main():
    string1 = stdin.readline().strip()
    string2 = stdin.readline().strip()
    result = isPermutation(string1, string2)
    if result:
        print('true')
    else:
        print('false')



if __name__ == '__main__':
    main()