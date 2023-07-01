num = input()
even_sum = 0
odd_sum = 0
for i in num:
    i = int(i)
    if i % 2 == 0:
        even_sum += i 
    else:
        odd_sum += i
print(even_sum, odd_sum)