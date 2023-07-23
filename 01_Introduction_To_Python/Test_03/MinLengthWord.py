def min_len_word(string):
    word_list = string.split(' ')
    min_length_word = word_list[0]
    for word in word_list:
        if len(word) < len(min_length_word):
            min_length_word = word
    return min_length_word



string = input()
result = min_len_word(string)
print(result)      