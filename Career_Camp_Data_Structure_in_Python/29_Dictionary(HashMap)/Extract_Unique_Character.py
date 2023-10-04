def unique_character(input_string):
    freq_count = ''
    for k in input_string:
        if k not in freq_count:
            freq_count += k
    return freq_count


def main():
    s = input()
    res = unique_character(s)
    print(res)

main()

# Input: ababacd
# Output: abcd