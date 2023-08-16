print('Secure connection established...')

try:
    principle_amount = int(input('Enter principle amount: '))
    duration = int(input('Enter duration: '))
    rate = int(input('Enter tha rate: '))
except:
    print('Enter Numerical Value...')
else:
    simple_interest = (principle_amount * duration * rate) / 100
    print('Simple Interest:', simple_interest)

print("Secure connection closed!")