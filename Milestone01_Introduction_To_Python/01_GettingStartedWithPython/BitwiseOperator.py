'''
Bitwise operator are use to compare binary number
Name            ---->           Operator
1. AND          ---->               &
2. OR           ---->               |
3. XOR          ---->               ^
4. NOT          ---->               ~
5. RIGHT SHIFT  ---->               >> 
6. LEFT SHIFT   ---->               <<
'''

x = 10 #Binary equivalent 01010
y = 20 #Binary equivalent 10100

#bitwise and operator
print(x & y)

#bitwise or operator
print(x | y)

#bitwise Xor operator
print(x ^ y)

#bitwise not operator
print(~x)

#bitwise leftshit operator
print(x << 2)  #2 is number of digit you want to shift

#bitwise right shift operator
print(x >> 2)