def isPossibleInterpretation(word:str, interpretation:str):
    i = 0
    j = 0
    while i < len(word) and j < len(interpretation):
        
        if word[i] != interpretation[j]:
            return False
        
        count_words = 1
        count_interpretation = 1

        while (i+1 < len(word)) and (word[i] == word[i+1]):
            count_words += 1
            i += 1
        while j+1 < len(interpretation) and interpretation[j] == interpretation[j+1]:
            count_interpretation += 1
            j += 1
        if count_words > count_interpretation:
            return False
        i += 1
        j += 1
    return i == len(word) and j == len(interpretation)



def take_input():
    '''function will take user input'''
    user_input = input()
    key_generated = input()
    return user_input, key_generated


def main():
    t = int(input())
    while t > 0:
        user_input, keyboard_generated = take_input()
        result = isPossibleInterpretation(user_input, keyboard_generated)
        if result:
            print('true')
        else:
            print('false')
        t -= 1


if __name__ == '__main__':
    main()

'''
2
code
cooodeee
hello
hheeeloo
'''