def check_num_seq(num):
    ''' Function return the Boolean value'''
    flag = True
    lst = taking_input(num)
    for i in range(num-2):
        if lst[i] < lst[i+1] and lst[i+1] > lst[i+2]:
            flag = False
            break
    return str(flag).lower()


def taking_input(num):
    ''' Taking user input'''
    num_lst = []
    for n in range(num):
        num_lst.append(int(input()))
    return num_lst

if __name__ == "__main__":
    number = int(input())
    result = check_num_seq(number)
    print(result)

# n = 5
# 9
# 8
# 4
# 5
# 6